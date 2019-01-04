from .models import Track
from rest_framework import serializers


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        exclude = ('id', 'submitter',)
        read_only_fields = ('date_created', 'date_modified')