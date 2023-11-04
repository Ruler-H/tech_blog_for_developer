from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('list/<int:pk>/', views.postlist, name='postlist'),
    path('<int:pk>/', views.postdetail, name='postdetail'),
    path('edit/<int:pk>/', views.postedit, name='postedit'),
    path('write/', views.postwrite, name='postwrite'),
    path('delete/<int:pk>/', views.postdelete, name='postdelete'),
    path('search/<int:pk>/', views.postlist, name='postsearch'),
    path('comment_add/<int:post_pk>/', views.comment_add, name='comment_add'),
    path('comment_delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
    path('comment_edit/<int:pk>/', views.comment_edit, name='comment_edit'),
    path('recomment_add/', views.recomment_add, name='recomment_add'),
    path('recomment_delete/<int:recomment_pk>/', views.recomment_delete, name='recomment_delete'),
    path('recomment_eidt/<int:pk>/', views.recomment_edit, name='recomment_edit'),
    path('other/<int:other_pk>/', views.other_postlist, name='other_postlist'),
]