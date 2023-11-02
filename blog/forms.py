from django import forms

from .models import Comment, Recomment

class CommentAddForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']


class RecommentAddForm(forms.ModelForm):

    class Meta:
        model = Recomment
        fields = ['content']