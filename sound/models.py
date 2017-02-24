from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from unidecode import unidecode


class Genre(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30, blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField()
    slug = models.SlugField()
    source = models.FileField(upload_to='songs_source')
    picture = models.ImageField(upload_to='songs_picture', blank=True)

    def get_absolute_url(self):
        return reverse('song-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class CommentSong(models.Model):
    song = models.ForeignKey(Song)
    author = models.ForeignKey(User)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:10]
