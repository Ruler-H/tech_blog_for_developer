from django.shortcuts import render
from django.views.generic import ListView
from .models import Board_Post

class BoardListView(ListView):
    model = Board_Post


boardlist = BoardListView.as_view()
