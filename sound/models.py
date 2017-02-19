from django.db import models
from django.template.defaultfilters import slugify


class Album(models.Model):
    title = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30, blank=True, null=True)
    genre = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='albums_logo')
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    source = models.FileField(upload_to='songs_source')
    album = models.ForeignKey(Album, blank=True, null=True)
    plays = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



