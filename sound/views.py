from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse

from .models import Song, Album, CommentSong


class IndexView(generic.ListView):
    template_name = 'sound/index.html'
    queryset = Album.objects.order_by('-likes')[:5]
    context_object_name = 'album_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['song_list'] = Song.objects.order_by('-likes')[:4]
        context['recent_song_list'] = Song.objects.order_by('-pub_date')[:4]
        return context


class SongDetailView(generic.DetailView):
    template_name = 'sound/song.html'
    model = Song


class CreateCommentSong(generic.View):
    template_name = 'sound/snippets/comments_list.html'

    def get(self, request):
        song_id = request.GET.get('song_id')
        author_name = request.GET.get('author_name')
        text = request.GET.get('text_body').strip()

        song = Song.objects.get(id=int(song_id))

        user = User.objects.get(username=author_name)
        comment = CommentSong(song=song,
                              author=user,
                              text=text)
        comment.save()
        return render(request, self.template_name, {'song': song})


class AddLike(generic.View):

    def get(self, request):
        song_id = request.GET.get('song_id')
        song = Song.objects.get(id=song_id)

        if song_id in request.session:
            song.likes -= 1
            del request.session[song_id]
        else:
            song.likes += 1
            request.session[song_id] = True

        song.save()
        return HttpResponse(song.likes)
