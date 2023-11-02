from django.forms import ModelForm

from .models import Board_Post

class BoardListForm(ModelForm):

    class Meta:
        model = Board_Post
        field = []