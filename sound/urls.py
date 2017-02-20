from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^songs/(?P<slug>[\w\-]+)/$', views.SongDetailView.as_view(), name='song-detail'),

]