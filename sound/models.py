from django.db import models
from django.template.defaultfilters import slugify


class Genre(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30, blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    logo = models.ImageField(upload_to='albums_logo')
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30, blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    source = models.FileField(upload_to='songs_source')
    album = models.ForeignKey(Album, blank=True, null=True)
    plays = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    picture = models.ImageField(upload_to='songs_picture', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



