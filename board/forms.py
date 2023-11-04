from typing import Any
from django import forms
from django.forms import ModelForm

from .models import Board_Post

class BoardWriteForm(ModelForm):

    title = forms.CharField(max_length=100, error_messages={'required': '제목을 입력해주세요.'})
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '내용을 입력해주세요.'})

    class Meta:
        model = Board_Post
        fields = ['title', 'content', 'category', 'upload_file']