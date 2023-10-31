from django.urls import path
from . import views

urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('<int:pk>/', views.postdetail, name='postdetail'),
    path('edit/<int:pk>/', views.postedit, name='postedit'),
    path('write/', views.postwrite, name='postwrite'),
    path('delete/<int:pk>/', views.postdelete, name='postdelete'),
    path('search/', views.postlist, name='postsearch'),
    path('subscribe/', views.subscribe, name='subscribe'),
]