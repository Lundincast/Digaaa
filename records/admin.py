from django.contrib import admin
from .models import Track

class TrackAdmin(admin.ModelAdmin):
    list_display = ['track_title', 'track_artist', 'track_release_date', 'submitter']
    list_filter = ['track_artist']

admin.site.register(Track, TrackAdmin)