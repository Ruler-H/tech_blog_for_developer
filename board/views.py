from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Board_Post
from .forms import BoardWriteForm

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
    model = Board_Post


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
        return redirect('/board/write/')


board_list = BoardListView.as_view()
board_detail = BoardDetailView.as_view()
board_write = BoardWriteView.as_view()
