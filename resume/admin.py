from django.contrib import admin
from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'artist_name', 'download_count')
    search_fields = ('song_name', 'artist_name')
    list_filter = ('artist_name',)