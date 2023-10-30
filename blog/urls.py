from django.urls import path
from . import views

urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('<int:pk>/', views.postdetail, name='postdetail'),
    path('edit/<int:pk>/', views.postedit, name='postedit'),
    path('write/', views.postwrite, name='postwrite'),
    path('subscribe/', views.subscribe, name='subscribe'),
]