from typing import Any
from django.views import View
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Post, Category, Comment, Recomment
from accounts.models import User
from .forms import CommentWriteForm, RecommentWriteForm, CommentEditForm, RecommentEditForm, PostWriteForm, PostEditForm
import re


class PostListView(LoginRequiredMixin, ListView):
    '''
    블로그 Post 목록 View
    '''
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_user = User.objects.get(pk=self.kwargs['pk'])
        categories = Category.objects.all().filter(user=blog_user)
        context['categories'] = categories
        context['blog_account'] = blog_user
        return context

    def get_queryset(self):
        querySet = super().get_queryset()
        blog_user = User.objects.get(pk=self.kwargs['pk'])
        querySet = querySet.filter(author = blog_user)
        search_keyword = self.request.GET.get('keyword')
        category = self.request.GET.get('category')
        if category == 'All':
            category = ''
        if search_keyword or category:
            querySet = querySet.filter(
                Q(title__icontains=search_keyword) | 
                Q(content__icontains=search_keyword) &
                Q(category__category__icontains=category)).distinct()
            
        return querySet
    

class PostDetailView(DetailView):
    '''
    블로그 글 상세보기 View
    '''
    model = Post

    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)
        if not post:
            return render(request, 'blog/post_not_found.html')
        post.view_count += 1
        post.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        comment_list = []
        for comment in Comment.objects.filter(post=context['post']):
            recomments = Recomment.objects.filter(comment=comment)
            comment_list.append({
                'comment': comment,
                'recomments': recomments,
            })
        context['comment_list']= comment_list
        return context
    

class PostWriteView(LoginRequiredMixin, CreateView):
    '''
    블로그 글 작성 View
    '''
    login_url = '/accounts/login/'
    model = Post
    form_class = PostWriteForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        categories = Category.objects.all().filter(user=current_user)
        context['categories'] = categories
        return context
    
    def post(self, request, *args, **kwargs):
        form = PostWriteForm(request.POST)
        current_user = self.request.user
        if form.is_valid():
            post = form.save(commit=False)
            image = extract_image(post.content)
            post.author = current_user
            post.category = Category.objects.get(Q(category = request.POST.get('category')) & Q(user = current_user))
            post.image = image
            post.save()
            return redirect(post.get_absolute_url())
        return super().post(request, *args, **kwargs)
    

class PostEditView(LoginRequiredMixin, UpdateView):
    '''
    블로그 게시글 수정 View
    '''
    login_url = '/accounts/login/'
    model = Post
    form_class = PostEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        categories = Category.objects.all().filter(user=current_user)
        context['categories'] = categories
        post = Post.objects.get(pk = self.kwargs["pk"])
        context['post'] = post
        return context
    
    def get(self, request: HttpRequest, *args, **kwargs):
        current_user = self.request.user
        post = Post.objects.get(pk = self.kwargs["pk"])
        if post.author != current_user:
            return redirect('/')
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = PostWriteForm(request.POST)
        current_user = self.request.user
        if form.is_valid():
            post = form.save(commit=False)
            image = extract_image(post.content)
            post.author = current_user
            post.category = Category.objects.get(Q(category = request.POST.get('category')) & Q(user = current_user))
            post.image = image
            post.save()
            return redirect(post.get_absolute_url())
        return super().post(request, *args, **kwargs)
    

class PostDeleteView(LoginRequiredMixin, DeleteView):
    '''
    블로그 게시글 삭제 View
    '''
    login_url = '/accounts/login/'
    model = Post
    success_url = '/blog'

    def post(self, request, *args, **kwargs):
        current_user = self.request.user
        post = Post.objects.get(pk = self.kwargs["pk"])
        if post.author != current_user:
            return redirect('/')
        return super().post(request, *args, **kwargs)
    

class CommentAddView(LoginRequiredMixin, CreateView):
    '''
    블로그 게시글 -> 댓글 추가 View
    '''
    login_url = '/accounts/login'
    model = Comment
    form_class = CommentWriteForm
    template_name = 'blog/post_detail.html'

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.request.POST['post_pk'])
        form = CommentWriteForm(request.POST)
        if form.is_valid():
            user = request.user
            comment = form.save(commit=False)
            comment.author = user
            comment.post = post
            comment.save()
            return redirect(comment.post.get_absolute_url())
            
        return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        '''
        context 반환 시 post의 댓글 & 대댓글을  context에 추가
        '''
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.request.POST['post_pk'])
        context['post'] = post
        comment_list = []
        for comment in Comment.objects.filter(post=post):
            recomments = Recomment.objects.filter(comment=comment)
            comment_list.append({
                'comment': comment,
                'recomments': recomments,
        })
        context['comment_list'] = comment_list
        return context


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    '''
    블로그 게시글 삭제 View
    '''
    login_url = '/accounts/login'
    
    def post(self, request, *args, **kwargs):
        comment_pk = kwargs.get('comment_pk')
        del_comment = Comment.objects.get(pk = comment_pk)
        del_comment.delete()
        post = Post.objects.get(pk=request.POST.get('post_pk'))
        comment_list = []
        for comment in Comment.objects.filter(post=post):
            recomments = Recomment.objects.filter(comment=comment)
            comment_list.append({
                'comment': comment,
                'recomments': recomments,
        })
        context = {
            'post': post,
            'comment_list': comment_list,
        }
        return render(request, 'blog/post_detail.html', context)
    

class CommentEditView(LoginRequiredMixin, UpdateView):
    '''
    블로그 게시글 수정 View
    '''
    login_url = '/accounts/login/'
    model = Comment
    form_class = CommentEditForm
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        '''
        context 반환 시 post의 댓글 & 대댓글을  context에 추가
        '''
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.request.POST['post_pk'])
        context['post'] = post
        comment_list = []
        for comment in Comment.objects.filter(post=post):
            recomments = Recomment.objects.filter(comment=comment)
            comment_list.append({
                'comment': comment,
                'recomments': recomments,
        })
        context['comment_list'] = comment_list
        return context
    

class RecommentAddView(LoginRequiredMixin, CreateView):
    '''
    블로그 게시글 대댓글 작성 View
    '''
    login_url = '/accounts/login'
    model = Recomment
    form_class = RecommentWriteForm
    template_name = 'blog/post_detail.html'

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.request.POST['post_pk'])
        form = RecommentWriteForm(request.POST)
        if form.is_valid():
            user = request.user
            comment = Comment.objects.get(pk=request.POST.get('comment_pk'))
            recomment = form.save(commit=False)
            recomment.author = user
            recomment.comment = comment
            recomment.save()
            return redirect(comment.post.get_absolute_url())
        return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        '''
        context 반환 시 post의 댓글 & 대댓글을  context에 추가
        '''
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.request.POST['post_pk'])
        context['post'] = post
        comment_list = []
        for comment in Comment.objects.filter(post=post):
            recomment = Recomment.objects.filter(comment=comment)
            comment_list.append({
                'comment':comment,
                'recomments':recomment,
            })
        context['comment_list'] = comment_list
        return context
    

class RecommentDeleteView(LoginRequiredMixin, DeleteView):
    '''
    블로그 대댓글 삭제 View
    '''
    login_url = '/accounts/login'
    model = Recomment

    def post(self, request, *args, **kwargs):
        recomment_pk = kwargs.get('recomment_pk')
        del_recomment = Recomment.objects.get(pk = recomment_pk)
        del_recomment.delete()
        post = Post.objects.get(pk=request.POST.get('post_pk'))
        comment_list = []
        for comment in Comment.objects.filter(post=post):
            recomments = Recomment.objects.filter(comment=comment)
            comment_list.append({
                'comment': comment,
                'recomments': recomments,
        })
        context = {
            'post': post,
            'comment_list': comment_list,
        }
        return render(request, 'blog/post_detail.html', context)
    

class RecommentEditView(LoginRequiredMixin, UpdateView):
    '''
    블로그 대댓글 수정 View
    '''
    login_url = '/accounts/login'
    model = Recomment
    form_class = RecommentEditForm
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        '''
        context 반환 시 post의 댓글 & 대댓글을  context에 추가
        '''
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.request.POST['post_pk'])
        context['post'] = post
        comment_list = []
        for comment in Comment.objects.filter(post=post):
            recomment = Recomment.objects.filter(comment=comment)
            comment_list.append({
                'comment':comment,
                'recomments':recomment,
            })
        context['comment_list'] = comment_list
        return context


class OtherPostListView(ListView):
    '''
    다른 사람의 블로그 목록 View
    '''
    model = Post
    ordering = '-updated_at'

    def get_queryset(self):
        querySet = super().get_queryset()
        other_pk = self.kwargs['other_pk']
        print(other_pk)
        other_user = User.objects.get(pk=other_pk)
        
        querySet = querySet.filter(author = other_user)
        search_keyword = self.request.GET.get('q')
        category = self.request.GET.get('category')
        if category == 'All':
            category = ''
        if search_keyword or category:
            querySet = querySet.filter(
                Q(title__icontains=search_keyword) | 
                Q(content__icontains=search_keyword) &
                Q(category__category__icontains=category)).distinct()
            
        return querySet
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_user = User.objects.get(pk=self.kwargs['other_pk'])
        categories = Category.objects.all().filter(user=blog_user)
        context['categories'] = categories
        context['blog_account'] = blog_user
        return context


postlist = PostListView.as_view()
post_detail = PostDetailView.as_view()
postedit = PostEditView.as_view()
postwrite = PostWriteView.as_view()
postdelete = PostDeleteView.as_view()
comment_add = CommentAddView.as_view()
comment_delete = CommentDeleteView.as_view()
comment_edit = CommentEditView.as_view()
recomment_add = RecommentAddView.as_view()
recomment_delete = RecommentDeleteView.as_view()
recomment_edit = RecommentEditView.as_view()
other_postlist = OtherPostListView.as_view()

def extract_image(content):
    image_list = re.findall('<img src=".+">', content)
    if image_list:
        return image_list[0][10:-2]