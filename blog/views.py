from typing import Any
from django.views import View
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Post, Image, Category, Comment, Recomment
import re

class SubscribeView(View):

    def get(self, request):
        return render(request, 'blog/subscribe.html')
    

class PostListView(ListView):
    model = Post
    ordering = '-updated_at'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        print('get_context_data')
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        categories = Category.objects.all().filter(user=current_user)
        context['categories'] = categories
        return context

    def get_queryset(self):
        querySet = super().get_queryset()
        current_user = self.request.user
        querySet = querySet.filter(author = current_user)
        print('get_queryset')
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
    

class PostDetailView(DetailView):
    model = Post

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)
        if not post:
            return render(request, 'blog/post_not_found.html')
        post.view_count += 1
        post.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(PostDetailView, self).get_context_data(**kwargs)
        images = Image.objects.all().filter(post=context['post'])
        context['images'] = images
        comment_list = []
        for comment in Comment.objects.filter(post=context['post']):
            recomment = Recomment.objects.filter(comment=comment)
            comment_list.append([comment, recomment])
        context['comment_list']= comment_list
        return context
    

class PostWriteView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Post
    fields = ['title', 'content', 'upload_file', 'category']

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        categories = Category.objects.all().filter(user=current_user)
        context['categories'] = categories
        return context
    
    def post(self, request, *args, **kwargs):
        current_user = self.request.user
        title = request.POST.get('title')
        content = request.POST.get('post-content')
        extract_image(content)
        upload_file = request.POST.get('upload_file')
        category = Category.objects.get(Q(category = request.POST.get('category')) & Q(user = current_user))
        write_post = Post.objects.create(title=title, content=content, upload_file=upload_file, category=category, author=current_user)
        write_post.save()

        return redirect(write_post.get_absolute_url())
    

class PostEditView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Post
    fields = ['title',  'content', 'upload_file', 'category']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        categories = Category.objects.all().filter(user=current_user)
        context['categories'] = categories
        post = Post.objects.get(pk = self.kwargs["pk"])
        context['post'] = post
        return context
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        current_user = self.request.user
        post = Post.objects.get(pk = self.kwargs["pk"])
        if post.author != current_user:
            return redirect('/')
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        current_user = self.request.user
        oldPost = Post.objects.get(pk = self.kwargs["pk"])
        if oldPost.author != current_user:
            return redirect('/')
        category = Category.objects.get(Q(category = request.POST.get('category')) & Q(user = current_user))
        title = request.POST.get('title')
        content = request.POST.get('post-content')
        upload_file = request.POST.get('upload_file')
        
        oldPost.title = title
        oldPost.content = content
        oldPost.upload_file = upload_file
        oldPost.category = category
        oldPost.save()

        return redirect(oldPost.get_absolute_url())
    

class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Post
    success_url = '/blog'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        current_user = self.request.user
        post = Post.objects.get(pk = self.kwargs["pk"])
        if post.author != current_user:
            return redirect('/')
        return super().post(request, *args, **kwargs)


subscribe = SubscribeView.as_view()
postlist = PostListView.as_view()
postdetail = PostDetailView.as_view()
postedit = PostEditView.as_view()
postwrite = PostWriteView.as_view()
postdelete = PostDeleteView.as_view()

def extract_image(content):
    image_list = re.findall('<img src=".+">', content)
    for image in image_list:
        print(image)
        image_name = image.split('src=')[-1][:-1]
        print(image_name)