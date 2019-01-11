from django.contrib import admin
from .models import Artist

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['artist_name', 'label_name', 'submitter', 'date_created']


admin.site.register(Artist, ArtistAdmin)