from django import forms
from django.forms import ModelForm

from .models import Post, Comment, Recomment

class PostWriteForm(ModelForm):
    '''
    블로그 게시글 작성 폼
    '''
    title = forms.CharField(max_length=100, error_messages={'required': '제목을 입력해주세요.'})
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '내용을 입력해주세요.'})
    category = forms.CharField(max_length=100, error_messages={'required': '카테고리를 입력해주세요.'})

    class Meta:
        model = Post
        fields = ['title', 'content', 'upload_file']


class PostEditForm(ModelForm):
    '''
    블로그 게시글 작성 폼
    '''
    title = forms.CharField(max_length=100, error_messages={'required': '제목을 입력해주세요.'})
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '내용을 입력해주세요.'})
    category = forms.CharField(max_length=100, error_messages={'required': '카테고리를 입력해주세요.'})

    class Meta:
        model = Post
        fields = ['title', 'content', 'upload_file']


class CommentWriteForm(ModelForm):
    '''
    게시글 댓글 작성 폼
    '''
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '댓글을 입력해주세요.'})

    class Meta:
        model = Comment
        fields = ['content']

    
class CommentEditForm(ModelForm):
    '''
    게시글 댓글 수정 폼
    '''
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '댓글을 입력해주세요.'})

    class Meta:
        model = Comment
        fields = ['content']


class RecommentWriteForm(ModelForm):
    '''
    게시글 대댓글 작성 폼
    '''
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '답글을 입력해주세요.'})

    class Meta:
        model = Recomment
        fields = ['content']


class RecommentEditForm(ModelForm):
    '''
    게시글 대댓글 수정 폼
    '''
    content = forms.CharField(widget=forms.Textarea, error_messages={'required': '답글을 입력해주세요.'})

    class Meta:
        model = Recomment
        fields = ['content']