from django.conf.urls import url
from . import views


urlpatterns = [

    # /
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_like/$', views.AddLike.as_view(), name='add-like'),

    # /songs/time/
    url(r'^songs/(?P<slug>[\w\-]+)/$',
        views.SongDetailView.as_view(),
        name='song-detail'),

    url(r'^add_comment/$',
        views.CreateCommentSong.as_view(),
        name='comment-create'),

    url(r'^suggestion/$',
        views.Suggestion.as_view(),
        name='suggestion'),

    url(r'^search/$',
        views.SearchView.as_view(),
        name='search'),

    url(r'^add_song/$',
        views.CreateSong.as_view(),
        name='create-song'),

    url(r'songs/(?P<slug>[\w\-]+)/update/$',
        views.UpdateSong.as_view(),
        name='update-song'),

]