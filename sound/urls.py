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



]