from django.contrib import admin
from .models import Album, Song, Genre, CommentSong


class CommentInline(admin.StackedInline):
    model = CommentSong

class AlbumAdmin(admin.ModelAdmin):
    exclude = ('likes', )
    prepopulated_fields = {'slug': ('title', )}

class SongAdmin(admin.ModelAdmin):
    exclude = ('likes', 'plays', )
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Genre, GenreAdmin)