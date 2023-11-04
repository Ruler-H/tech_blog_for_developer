from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Board_Post

class BoardListView(ListView):
    model = Board_Post
    ordering = '-pk'


class BoardDetailView(DetailView):
    model = Board_Post



board_list = BoardListView.as_view()
board_detail = BoardDetailView.as_view()
