from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('<int:pk>/', views.board_detail, name='board_detail'),
    path('write/', views.board_write, name='board_write'),
    path('edit/<int:pk>/', views.board_edit, name='board_edit'),
    path('delete/<int:pk>/', views.board_delete, name='board_delete'),
    path('comment/write/', views.comment_write, name='comment_write'),
    path('comment/edit/<int:pk>/', views.comment_edit, name='comment_edit'),
    path('comment/delete/<int:pk>/', views.comment_delete, name='comment_delete'),
    path('recomment/write/', views.recomment_write, name='recomment_write'),
    path('recomment/edit/<int:pk>/', views.recomment_edit, name='recomment_edit'),
]