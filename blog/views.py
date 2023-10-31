from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.db.models import Q

from .models import Post, Image, Category

class SubscribeView(View):

    def get(self, request):
        return render(request, 'blog/subscribe.html')
    

class PostListView(ListView):
    model = Post
    ordering = '-updated_at'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        categories = Category.objects.all().filter(user=current_user)
        context['categories'] = categories
        return context

    def get_queryset(self):
        querySet = super().get_queryset()
        current_user = self.request.user
        querySet = querySet.filter(author = current_user)
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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(PostDetailView, self).get_context_data(**kwargs)
        images = Image.objects.all().filter(post=context['post'])
        context['images'] = images
        return context
class PostWriteView(CreateView):
    
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
        upload_file = request.POST.get('upload_file')
        category = Category.objects.get(Q(category = request.POST.get('category')) & Q(user = current_user))
        write_post = Post.objects.create(title=title, content=content, upload_file=upload_file, category=category, author=current_user)
        write_post.save()

        return redirect(write_post.get_absolute_url())
    

class PostEditView(UpdateView):
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
    
    def post(self, request, *args, **kwargs):
        current_user = self.request.user
        oldPost = Post.objects.get(pk = self.kwargs["pk"])
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
    

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)


subscribe = SubscribeView.as_view()
postlist = PostListView.as_view()
postdetail = PostDetailView.as_view()
postedit = PostEditView.as_view()
postwrite = PostWriteView.as_view()
postdelete = PostDeleteView.as_view()