from typing import Any
from django.core.handlers.wsgi import WSGIRequest
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.shortcuts import render, redirect
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.hashers import check_password
import re

from .models import User
from .forms import SubscribeForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = ''

    def post(self, request: HttpRequest, *args, **kwargs):
        return super(CustomLoginView, self).post(request, *args, **kwargs)

class SignUpView(CreateView):
    model = User
    template_name = 'accounts/signup.html'
    fields = ['username', 'nickname', 'email', 'password', 'development_field', 'phone']

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.POST.get('username')
        context = {}
        if not username:
            context['notice'] = '유저명은 필수 입력 값입니다.'
            return render(request, 'accounts/signup.html', context)
        nickname = request.POST.get('nickname')
        if not nickname:
            context['notice'] = '닉네임은 필수 입력 값입니다.'
            return render(request, 'accounts/signup.html', context)
        email = request.POST.get('email')
        if not email:
            context['notice'] = '이메일은 필수 입력 값입니다.'
            return render(request, 'accounts/signup.html', context)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        message = passwordValidator(password1, password2)
        if message:
            context['notice'] = message
            return render(request, 'accounts/signup.html', context)
        development_field = request.POST.get('development_field')
        if not development_field:
            context['notice'] = '개발 분야은 필수 입력 값입니다.'
            return render(request, 'accounts/signup.html', context)
        phone = request.POST.get('phone')
        user = User(username=username, nickname=nickname, email=email, development_field=development_field, phone=phone)
        user.set_password(password1)
        user.save()
        return redirect('/accounts/login')
    

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    login_url = '/accounts/login/'
    next_page = '/accounts/login/'


class ProfileView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        return render(request, 'accounts/profile.html')
    

class ProfileEditView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = User
    fields = ['nickname', 'development_field', 'phone', 'profile_image']
    template_name = 'accounts/profile_edit.html'
    
    success_url = '/accounts/profile/'

    def post(self, request: HttpRequest, *args, **kwargs):
        context = {}
        nickname = request.POST.get('nickname')
        if not nickname:
            context['notice'] = '닉네임은 필수 입력 값입니다.'
            return render(request, 'accounts/profile_edit.html', context)
        development_field = request.POST.get('development_field')
        if not development_field:
            context['notice'] = '개발 분야은 필수 입력 값입니다.'
            return render(request, 'accounts/profile_edit.html', context)
        phone = request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')
        user = User.objects.get(pk = request.user.pk)
        user.nickname = nickname
        user.development_field = development_field
        user.phone = phone
        if profile_image:
            user.profile_image = profile_image
        user.save()
        return redirect('/accounts/profile/')


class PasswordChangeView(View):

    def get(self, request):
        return render(request, 'accounts/password_change.html')
    
    def post(self, request):
        cur_password = request.POST.get('cur_password')
        context = {}
        if not check_password(cur_password, request.user.password):
            context['notice'] = '현재 비밀번호가 일치하지 않습니다.'
            return render(request, 'accounts/password_change.html', context)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        message = passwordValidator(password1, password2)
        if message:
            context['notice'] = message
            return render(request, 'accounts/password_change.html', context)
        user = request.user
        user.set_password(password1)
        user.save()
        auth.logout(request)
        return redirect('/accounts/login')
    

class SubscribeView(LoginRequiredMixin, ListView):
    model = User
    form_class = SubscribeForm
    login_url = '/accounts/login/'


class SubscribeDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    form_class = SubscribeForm
    login_url = '/accounts/login/'

    def post(self, request: HttpRequest, *args, **kwargs):
        sub_pk = kwargs.get("subscription_pk")
        user = request.user
        subscription = user.subscriptions.get(pk=sub_pk)
        user.subscriptions.remove(subscription)
        user.save()
        return redirect('/accounts/subscribe/')
    

class SubscribeManageView(LoginRequiredMixin, UpdateView):
    '''
    구독 관리 View
    구독되어 있는 경우 해제
    구독안되어 있는 경우 추가
    '''
    model = User
    login_url = '/accounts/login/'
    template_name = 'blog/post_list.html'
    fields = ['subscriptions']

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        '''
        post 요청이 올 경우
        현재 요청 유저의 subscriptions 목록을 확인하여
        목록에 포함되어 있는 경우 구독 해제
        목록에 없는 경우 구독
        '''
        subscription_pk = kwargs.get('pk')
        subscription_user = User.objects.get(pk=subscription_pk)
        current_user = request.user
        
        if subscription_user in current_user.subscriptions.all():
            current_user.subscriptions.remove(subscription_user)
        else:
            current_user.subscriptions.add(subscription_user)
        
        current_user.save()
        
        return HttpResponse('subscription manage success')



def passwordValidator(password1, password2):
    if password1 != password2:
        return '입력된 비밀번호가 다릅니다.'
    if len(password1) < 8:
        return '비밀번호는 8자리 이상이어야 합니다.'
    if not re.search(r"[a-zA-Z]", password1):
        return '비밀번호는 하나 이상의 영문이 포함되어야 합니다.'
    if not re.search(r"\d", password1):
        return '비밀번호는 하나 이상의 숫자가 포함되어야 합니다.'
    if not re.search(r"[!@#$%^&*()]", password1):
        return '비밀번호는 적어도 하나 이상의 특수문자(!@#$%^&*())가 포함되어야 합니다.'
    
login = CustomLoginView.as_view()
signup = SignUpView.as_view()
logout = CustomLogoutView.as_view()
profile = ProfileView.as_view()
profile_edit = ProfileEditView.as_view()
password_change = PasswordChangeView.as_view()
subscribe = SubscribeView.as_view()
subscribe_delete = SubscribeDeleteView.as_view()
subscribe_manage = SubscribeManageView.as_view()