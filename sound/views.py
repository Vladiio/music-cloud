from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Song, Album


class IndexView(generic.ListView):
    template_name = 'sound/index.html'
    queryset = Album.objects.order_by('-likes')[:5]
    context_object_name = 'album_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['song_list'] = Song.objects.order_by('-likes')[:5]
        context['recent_song_list'] = Song.objects.order_by('-pub_date')[:5]
        return context


class SongDetailView(generic.DetailView):
    template_name = 'sound/song.html'
    model = Song



