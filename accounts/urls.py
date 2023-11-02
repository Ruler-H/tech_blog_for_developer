from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/<int:pk>/', views.profile_edit, name='profile_edit'),
    path('profile/password_change/', views.password_change, name='password_change'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribe/delete/<int:subscription_pk>/', views.subscribe_delete, name='subscribe_delete'),
]