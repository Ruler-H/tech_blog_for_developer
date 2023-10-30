from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.db.models import Q

from .models import Post, Image, Category

class SubscribeView(View):

    def get(self, request):
        return render(request, 'blog/subscribe.html')
    

class PostListView(ListView):
    model = Post
    ordering = '-pk'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        print(super().get_context_data(**kwargs))
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        querySet = super().get_queryset()
        current_user = self.request.user
        querySet = querySet.filter(author = current_user)
        print(querySet)
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
        print(request.POST)
        content = request.POST.get('content')
        upload_file = request.POST.get('upload_file')
        category = Category.objects.get(Q(user=current_user) & Q(category = request.POST.get('category')))
        write_post = Post.objects.create(title=title, content=content, upload_file=upload_file, category=category, author=current_user)
        write_post.save()

        return redirect(write_post.get_absolute_url())
    

class PostEditView(UpdateView):
    model = Post
    fields = ['title',  'content', 'upload_file', 'category']




subscribe = SubscribeView.as_view()
postlist = PostListView.as_view()
postdetail = PostDetailView.as_view()
postedit = PostEditView.as_view()
postwrite = PostWriteView.as_view()