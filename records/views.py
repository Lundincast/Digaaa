from .models import Track, Album
from rest_framework import viewsets, permissions
from .serializers import TrackSerializer, AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tracks to be viewed or edited.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Track.objects.filter(submitter=self.request.user)

    def perform_create(self, serializer):
        serializer.save(submitter=self.request.user)


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows albums to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Album.objects.filter(submitter=self.request.user)

    def perform_create(self, serializer):
        serializer.save(submitter=self.request.user)