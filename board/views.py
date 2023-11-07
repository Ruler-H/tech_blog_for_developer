from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
import re

from .models import Board_Post, Board_Comment, Board_Recomment
from .forms import BoardWriteForm, BoardEditForm, CommentWriteForm, CommentEditForm, RecommentWriteForm, RecommentEditForm

class BoardListView(ListView):
    '''
    게시판 게시글 목록 View
    '''
    model = Board_Post
    ordering = '-pk'

    def get_queryset(self):
        querySet = super().get_queryset()
        search_keyword = self.request.GET.get('keyword')
        category = self.request.GET.get('category')
        if category == 'All':
            category = ''
        if search_keyword or category:
            querySet = querySet.filter(
                Q(title__icontains=search_keyword) | 
                Q(content__icontains=search_keyword) &
                Q(category__icontains=category)).distinct()
            
        return querySet


class BoardDetailView(DetailView):
    '''
    게시글 상세보기 View
    '''
    model = Board_Post

    def get(self, request, *args, **kwargs):
        '''
        상세보기 get 요청 시 조회수 증가
        '''
        board_post = Board_Post.objects.get(pk=self.kwargs['pk'])
        board_post.view_count += 1
        board_post.save()
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        '''
        context 반환 시 post의 댓글 & 대댓글을  context에 추가
        '''
        context = super().get_context_data(**kwargs)
        board_post = Board_Post.objects.get(pk=self.kwargs['pk'])
        comment_list = []
        for comment in Board_Comment.objects.filter(board_post=board_post):
            recomment = Board_Recomment.objects.filter(board_comment=comment)
            comment_list.append({
                'comment':comment,
                'recomments':recomment,
            })
        context['comment_list'] = comment_list
        return context


class BoardWriteView(LoginRequiredMixin, CreateView):
    '''
    게시판 글 작성 View
    '''
    login_url = '/accounts/login/'
    model = Board_Post
    form_class = BoardWriteForm

    def post(self, request, *args, **kwargs):
        form = BoardWriteForm(request.POST)
        if form.is_valid():
            board_post = form.save(commit=False)
            board_post.author = request.user
            board_post.image = extract_image(board_post.content)
            board_post.upload_file = request.FILES.get('upload_file')
            board_post.save()
            return redirect(board_post.get_absolute_url())
        return super().post(request, *args, **kwargs)
    

class BoardEditView(LoginRequiredMixin, UpdateView):
    '''
    게시판 게시글 수정 View
    '''
    login_url = '/accounts/login/'
    model = Board_Post
    form_class = BoardEditForm
    def post(self, request, *args, **kwargs):
        form = BoardEditForm(request.POST)
        print(form)
        if form.is_valid():
            board_post = Board_Post.objects.get(pk = self.kwargs["pk"])
            board_post.title = request.POST.get('title')
            board_post.content = request.POST.get('content')
            board_post.author = request.user
            image = extract_image(board_post.content)
            board_post.upload_file = request.FILES.get('upload_file')
            if image:
                board_post.image = image
            board_post.save()
            return redirect(board_post.get_absolute_url())
        return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = 'edit'
        return context


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    '''
    게시글 삭제 View
    [x] success url 설정
    '''
    login_url = '/accounts/login/'
    model = Board_Post
    success_url = '/board/'


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    '''
    게시글 댓글 삭제 View
    '''
    login_url = '/accounts/login/'
    model = Board_Comment
    
    def get_success_url(self):
        '''
        삭제 완료 시 redirect를 위한 success url
        '''
        post_pk = self.request.POST.get('post_pk')
        board_post = Board_Post.objects.get(pk=post_pk)
        return board_post.get_absolute_url()


class CommentEditView(LoginRequiredMixin, UpdateView):
    '''
    게시글 댓글 수정 View
    '''
    login_url = '/accounts/login/'
    model = Board_Comment
    form_class = CommentEditForm
    template_name = 'board/board_post_detail.html'

    def get_context_data(self, **kwargs):
        '''
        context 반환 시 post의 댓글 & 대댓글을  context에 추가
        '''
        context = super().get_context_data(**kwargs)
        board_post = Board_Post.objects.get(pk=self.request.POST['post_pk'])
        context['board_post'] = board_post
        comment_list = []
        for comment in Board_Comment.objects.filter(board_post=board_post):
            recomment = Board_Recomment.objects.filter(board_comment=comment)
            comment_list.append({
                'comment':comment,
                'recomments':recomment,
            })
        context['comment_list'] = comment_list
        return context


class CommentWriteView(LoginRequiredMixin, CreateView):
    '''
    게시글 댓글 작성 View
    '''
    login_url = '/accounts/login/'
    model = Board_Comment
    form_class = CommentWriteForm
    template_name = 'board/board_post_detail.html'

    def post(self, request, *args, **kwargs):
        '''
        댓글 작성 시 유효성을 검사
        유효성 통과 시 댓글을 저장
        '''
        form = CommentWriteForm(request.POST)
        board_post = Board_Post.objects.get(pk=request.POST['post_pk'])
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.board_post = board_post
            comment.save()
            return redirect(board_post.get_absolute_url())
        
        return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        '''
        context 반환 시 post의 댓글 & 대댓글을  context에 추가
        '''
        context = super().get_context_data(**kwargs)
        board_post = Board_Post.objects.get(pk=self.request.POST['post_pk'])
        context['board_post'] = board_post
        comment_list = []
        for comment in Board_Comment.objects.filter(board_post=board_post):
            recomment = Board_Recomment.objects.filter(board_comment=comment)
            comment_list.append({
                'comment':comment,
                'recomments':recomment,
            })
        context['comment_list'] = comment_list
        return context


class RecommentWriteView(LoginRequiredMixin, CreateView):
    '''
    게시글 대댓글 작성 View
    [x] 대댓글 작성 구현 필요
    '''
    login_url = '/accounts/login'
    model = Board_Recomment
    form_class = RecommentWriteForm
    template_name = 'board/board_post_detail.html'

    def post(self, request, *args, **kwargs):
        form = RecommentWriteForm(request.POST)
        if form.is_valid():
            recomment = form.save(commit=False)
            recomment.author = request.user
            recomment.board_comment = Board_Comment.objects.get(pk=request.POST['comment_pk'])
            recomment.save()
            return redirect(recomment.get_absolute_url())
        return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        '''
        context 반환 시 post의 댓글 & 대댓글을  context에 추가
        '''
        context = super().get_context_data(**kwargs)
        board_post = Board_Post.objects.get(pk=self.request.POST['post_pk'])
        context['board_post'] = board_post
        comment_list = []
        for comment in Board_Comment.objects.filter(board_post=board_post):
            recomment = Board_Recomment.objects.filter(board_comment=comment)
            comment_list.append({
                'comment':comment,
                'recomments':recomment,
            })
        context['comment_list'] = comment_list
        return context


class RecommentEditView(LoginRequiredMixin, UpdateView):
    '''
    게시판 대댓글 수정 View
    '''
    login_url = '/accounts/login'
    model = Board_Recomment
    form_class = RecommentEditForm
    template_name = 'board/board_post_detail.html'

    def get_context_data(self, **kwargs):
        '''
        context 반환 시 post의 댓글 & 대댓글을  context에 추가
        '''
        context = super().get_context_data(**kwargs)
        board_post = Board_Post.objects.get(pk=self.request.POST['post_pk'])
        context['board_post'] = board_post
        comment_list = []
        for comment in Board_Comment.objects.filter(board_post=board_post):
            recomment = Board_Recomment.objects.filter(board_comment=comment)
            comment_list.append({
                'comment':comment,
                'recomments':recomment,
            })
        context['comment_list'] = comment_list
        return context


class RecommentDeleteView(LoginRequiredMixin, DeleteView):
    '''
    게시판 대댓글 삭제 View
    '''
    login_url = '/accounts/login/'
    model = Board_Recomment

    def get_success_url(self):
        '''
        삭제 완료 시 redirect를 위한 success url
        '''
        post_pk = self.request.POST.get('post_pk')
        board_post = Board_Post.objects.get(pk=post_pk)
        return board_post.get_absolute_url()


board_list = BoardListView.as_view()
board_detail = BoardDetailView.as_view()
board_write = BoardWriteView.as_view()
board_edit = BoardEditView.as_view()
board_delete = BoardDeleteView.as_view()
comment_write = CommentWriteView.as_view()
comment_edit = CommentEditView.as_view()
comment_delete = CommentDeleteView.as_view()
recomment_write = RecommentWriteView.as_view()
recomment_edit = RecommentEditView.as_view()
recomment_delete = RecommentDeleteView.as_view()

def extract_image(content):
    '''
    content의 첫 이미지의 src를 리턴
    '''
    image_list = re.findall('<img src=".+">', content)
    if image_list:
        return image_list[0][10:-2]