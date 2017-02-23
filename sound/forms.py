from django import forms
from .models import CommentSong


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentSong
        fields = ('text', )
