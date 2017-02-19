from django.contrib import admin
from .models import Album, Song


class AlbumAdmin(admin.ModelAdmin):
    exclude = ('likes', )
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Album, AlbumAdmin)
