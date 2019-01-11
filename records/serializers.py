from .models import Track, Album
from artists.models import Artist
from rest_framework import serializers


class ArtistField(serializers.PrimaryKeyRelatedField):

    def get_queryset(self):
        user = self.context['request'].user
        queryset = Artist.objects.filter(submitter=user)
        return queryset


class TrackSerializer(serializers.ModelSerializer):
    artist = ArtistField(many=False)

    class Meta:
        model = Track
        exclude = ('id', 'submitter',)
        read_only_fields = ('date_created', 'date_modified')


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistField(many=False)
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        exclude = ('id', 'submitter',)
        read_only_fields = ('date_created', 'date_modified')