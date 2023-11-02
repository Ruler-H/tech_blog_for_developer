from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('<int:pk>/', views.postdetail, name='postdetail'),
    path('edit/<int:pk>/', views.postedit, name='postedit'),
    path('write/', views.postwrite, name='postwrite'),
    path('delete/<int:pk>/', views.postdelete, name='postdelete'),
    path('search/', views.postlist, name='postsearch'),
    path('comment_add/<int:post_pk>/', views.comment_add, name='comment_add'),
    path('comment_delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
    path('recomment_add/', views.recomment_add, name='recomment_add'),
    path('recomment_delete/<int:recomment_pk>/', views.recomment_delete, name='recomment_delete'),
    path('subscribe/', views.subscribe, name='subscribe'),
]