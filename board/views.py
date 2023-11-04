from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Board_Post

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



board_list = BoardListView.as_view()
board_detail = BoardDetailView.as_view()
