from django import forms

from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'nickname', 'email', 'password', 'development_field', 'phone']

    
class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']