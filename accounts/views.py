from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
import re

from .models import User
from .forms import UserForm, UserLoginForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = ''

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print(request.POST)
        return super(CustomLoginView, self).post(request, *args, **kwargs)

class SignUpView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/signup.html'
    success_url = 'accounts/login.html'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
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
        password = request.POST.get('password')
        password_conf = request.POST.get('password_conf')
        message = passwordValidator(password, password_conf)
        if message:
            context['notice'] = message
            return render(request, 'accounts/signup.html', context)
        development_field = request.POST.get('development_field')
        if not development_field:
            context['notice'] = '개발 분야은 필수 입력 값입니다.'
            return render(request, 'accounts/signup.html', context)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/accounts/login')


login = CustomLoginView.as_view()
signup = SignUpView.as_view()

def passwordValidator(password, password_conf):
    if password != password_conf:
        return '입력된 비밀번호가 다릅니다.'
    if len(password) < 8:
        return '비밀번호는 8자리 이상이어야 합니다.'
    if not re.search(r"[a-zA-Z]", password):
        return '비밀번호는 하나 이상의 영문이 포함되어야 합니다.'
    if not re.search(r"\d", password):
        return '비밀번호는 하나 이상의 숫자가 포함되어야 합니다.'
    if not re.search(r"[!@#$%^&*()]", password):
        return '비밀번호는 적어도 하나 이상의 특수문자(!@#$%^&*())가 포함되어야 합니다.'