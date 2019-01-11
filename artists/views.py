from .models import Artist
from rest_framework import viewsets, permissions
from .serializers import ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows artists to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Artist.objects.filter(submitter=self.request.user)

    def perform_create(self, serializer):
        serializer.save(submitter=self.request.user)