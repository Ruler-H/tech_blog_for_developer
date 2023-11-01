from django import forms

from .models import User
    
class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']