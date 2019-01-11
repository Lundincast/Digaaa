from .models import Artist
from rest_framework import serializers


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        exclude = ('id', 'submitter')
        read_only_fields = ('date_created', 'date_modified')