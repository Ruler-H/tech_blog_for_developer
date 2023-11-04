from django.forms import ModelForm

from .models import Comment, Recomment

class CommentAddForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content']


class RecommentAddForm(ModelForm):

    class Meta:
        model = Recomment
        fields = ['content']


class CommentEditForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

class RecommentEditForm(ModelForm):

    class Meta:
        model = Recomment
        fields = ['content']