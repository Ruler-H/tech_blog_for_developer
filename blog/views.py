from django.shortcuts import render
from django.views import View

class SubscribeView(View):

    def get(self, request):
        return render(request, 'blog/subscribe.html')
    

subscribe = SubscribeView.as_view()
