from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from blog.models import Post
from board.models import Board_Post

class IndexView(ListView):

    def get(self, request):
        
        blog_post_list = Post.objects.all().order_by('-pk')[:8]
        subscription_post_list = []
        if request.user.is_authenticated:
            for subscription in request.user.subscriptions.all():
                subscription_post_list += Post.objects.filter(author = subscription).order_by('-pk')[:1]
        board_post_list = Board_Post.objects.all().order_by('-pk')[:8]
        context = {
            'blog_post_list': blog_post_list,
            'subscription_post_list': subscription_post_list,
            'board_post_list': board_post_list,
        }
        return render(request, 'main/index.html', context)

index = IndexView.as_view()
