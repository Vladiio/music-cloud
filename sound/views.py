from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Song, Album


class IndexView(generic.ListView):
    template_name = 'sound/index.html'
    queryset = Album.objects.all()
    context_object_name = 'album_list'

