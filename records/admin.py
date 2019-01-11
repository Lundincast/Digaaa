from django.contrib import admin
from .models import Track

class TrackAdmin(admin.ModelAdmin):
    list_display = ['track_title', 'artist', 'track_release_date', 'submitter']
    list_filter = ['date_created']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_title', 'artist', 'date_created', 'submitter']

admin.site.register(Track, TrackAdmin)