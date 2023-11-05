from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Board_Post, Board_Comment, Board_Recomment
from .forms import BoardWriteForm, BoardEditForm

class BoardListView(ListView):
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
    게시글 상세보기
    '''
    model = Board_Post

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        '''
        상세보기 get 요청 시 조회수 증가
        '''
        board_post = Board_Post.objects.get(pk=self.kwargs['pk'])
        board_post.view_count += 1
        board_post.save()
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
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
    login_url = '/accounts/login/'
    model = Board_Post
    form_class = BoardWriteForm

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = BoardWriteForm(request.POST)
        print(form)
        if form.is_valid():
            board_post = form.save(commit=False)
            board_post.author = request.user
            board_post.save()
            return redirect(board_post.get_absolute_url())
        return super().post(request, *args, **kwargs)
    

class BoardEditView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Board_Post
    form_class = BoardEditForm
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = BoardEditForm(request.POST)
        print(form)
        board_post = form.save(commit=False)
        if form.is_valid():
            board_post.author = request.user
            board_post.save()
            return redirect(board_post.get_absolute_url())
        return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['url'] = 'edit'
        return context


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Board_Post


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Board_Comment


class CommentEditView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Board_Comment


board_list = BoardListView.as_view()
board_detail = BoardDetailView.as_view()
board_write = BoardWriteView.as_view()
board_edit = BoardEditView.as_view()
board_delete = BoardDeleteView.as_view()

comment_delete = CommentDeleteView.as_view()
comment_edit = CommentEditView.as_view()