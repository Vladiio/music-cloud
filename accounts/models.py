from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    web_site = models.URLField(blank=True)
    picture = models.ImageField(upload_to='user-profiles', blank=True)

    def __str__(self):
        return self.user.username


