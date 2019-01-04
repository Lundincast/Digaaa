from .models import Track
from rest_framework import viewsets, permissions
from .serializers import TrackSerializer


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