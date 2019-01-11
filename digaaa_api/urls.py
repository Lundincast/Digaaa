from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from artists.views import ArtistViewSet
from records.views import AlbumViewSet, TrackViewSet

router = DefaultRouter()
router.register('artists', ArtistViewSet)
router.register('albums', AlbumViewSet)
router.register('tracks', TrackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('dashboard/', include(router.urls)),
]
