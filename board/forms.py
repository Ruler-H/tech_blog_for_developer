from typing import Any
from django import forms
from django.forms import ModelForm

from .models import Board_Post, Board_Comment

class BoardWriteForm(ModelForm):
    '''
    게시판 게시글 작성 폼
    '''
    title = forms.CharField(max_length=100, error_messages={'required': '제목을 입력해주세요.'})
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '내용을 입력해주세요.'})

    class Meta:
        model = Board_Post
        fields = ['title', 'content', 'category', 'upload_file']


class BoardEditForm(ModelForm):
    '''
    게시판 게시글 수정 폼
    '''
    title = forms.CharField(max_length=100, error_messages={'required': '제목을 입력해주세요.'})
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '내용을 입력해주세요.'})

    class Meta:
        model = Board_Post
        fields = ['title', 'content', 'category', 'upload_file']


class CommentWriteForm(ModelForm):
    '''
    게시글 댓글 작성 폼
    '''
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '댓글을 입력해주세요.'})

    class Meta:
        model = Board_Comment
        fields = ['content']

    
class CommentEditForm(ModelForm):
    '''
    게시글 댓글 수정 폼
    '''
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '댓글을 입력해주세요.'})

    class Meta:
        model = Board_Comment
        fields = ['content']