from django import forms
from django.utils import timezone

from .models import Song


class SongCreateForm(forms.ModelForm):
    pub_date = forms.DateTimeField(widget=forms.HiddenInput(),initial=timezone.now())
    title = forms.CharField(max_length=30)

    class Meta:
        model = Song
        exclude = ('likes', 'slug')
