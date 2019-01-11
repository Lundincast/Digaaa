from django.db import models
from django.utils import timezone

from artists.models import Artist
from users.models import User
from common.models import ARTIST_ADD_CHOICES, LANGUAGE_CODES_CHOICES, TRACK_TYPE_CHOICES, TRACK_PREORDER_TYPE_CHOICES, GENRE_CHOICES, COUNTRY_CODES_CHOICES


class Album(models.Model):
    key = models.PositiveIntegerField(editable=False, blank=True)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.SET_NULL, blank=True, null=True)
    album_artist_add = models.CharField(blank=False, choices=ARTIST_ADD_CHOICES, max_length=50)
    album_title = models.CharField(blank=False, max_length=200)
    album_version = models.CharField(blank=True, max_length=200)
    label_name = models.CharField(blank = False, max_length=200)
    album_artist_url = models.CharField(blank=True, max_length=200)
    album_label_order_number = models.CharField(blank=True, null=False, max_length=200)
    album_media_type = models.CharField(blank=True, max_length=50)
    asis_types = models.CharField(blank=True, max_length=50)
    album_mfit_provider = models.CharField(blank=True, max_length=200)
    track_count = models.SmallIntegerField(blank=True, null=False)
    album_release_date = models.DateTimeField('album release date', blank=False)
    album_digital_release_date = models.DateTimeField('album digital release date', blank=False)
    album_price_group = models.CharField(blank=True, max_length=200)
    album_genre = models.CharField(blank=False, choices=GENRE_CHOICES, max_length=200)
    album_genre_2 = models.CharField(blank=True, choices=GENRE_CHOICES, max_length=200)
    distribution_territory = models.CharField(blank=False, choices=COUNTRY_CODES_CHOICES, max_length=10)
    album_preorder_release_date = models.DateTimeField('album preorder release date', blank=True)
    album_preorder_weeks = models.SmallIntegerField(blank=True, null=True)
    album_preorder_preview = models.BooleanField(default=False)
    album_preorder_price_group = models.CharField(blank=True, max_length=200)
    dont_deliver_to_shop = models.CharField(blank=True, null=True, max_length=200)
    only_deliver_to_shop = models.CharField(blank=True, null=True, max_length=200)
    allow_subscription_service = models.BooleanField(default=True)
    album_language = models.CharField(max_length=3, choices=LANGUAGE_CODES_CHOICES, default='en')
    album_copyright_info = models.CharField(blank=False, max_length=200)
    album_production_info = models.CharField(blank=False, max_length=200)
    booklet_included = models.BooleanField(default=False)
    liner_notes = models.CharField(blank=True, null=True, max_length=200)
    album_ean_upc = models.BigIntegerField(blank=False)
    submitter = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=False)
    date_created = models.DateTimeField(editable=False)
    date_modified = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        # set the key so that it's incremental on a per-user basis
        key = cal_key(self.submitter)
        self.key = key
        # update timestamps
        if not self.id:
            self.date_created = timezone.now()
        self.date_modified = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('album_detail', args=[str(self.id)])

    def __str__(self):
        return self.album_title


class Track(models.Model):
    key = models.PositiveIntegerField(editable=False, blank=True)
    artist = models.ForeignKey(Artist, related_name='tracks', on_delete=models.SET_NULL, blank=True, null=True)
    track_artist_add = models.CharField(blank=False, choices=ARTIST_ADD_CHOICES, max_length=200)
    track_title = models.CharField(blank=False, max_length=200)
    track_version = models.CharField(blank=True, null=True, max_length=100)
    track_duration = models.CharField(blank=True, null=False, max_length=8)
    track_prelisten_start_second = models.CharField(blank=True, null=True, max_length=8)
    track_number = models.SmallIntegerField(blank=True, null=True)
    set_number = models.SmallIntegerField(blank=False, default=1)
    set_name = models.CharField(blank=True, null=True, max_length=200)
    track_language = models.CharField(max_length=3, choices=LANGUAGE_CODES_CHOICES, default='en')
    track_live = models.BooleanField(default=False)
    track_type = models.CharField(blank=True, choices=TRACK_TYPE_CHOICES, max_length=200)
    track_sale_allowed = models.BooleanField(default=False)
    track_price_group = models.CharField(blank=True, max_length=10)
    track_release_date = models.DateTimeField('track release date', blank=True, null=True)
    track_digital_release_date = models.DateTimeField('track digital release date', blank=True, null=True)
    track_preorder_type = models.CharField(blank=True, null=True, choices=TRACK_PREORDER_TYPE_CHOICES, max_length=50)
    instant_grat_start_date = models.DateTimeField('instant grat start date', blank=True, null=True)
    track_genre = models.CharField(blank=False, choices=GENRE_CHOICES, max_length=50)
    track_genre_2 = models.CharField(blank=True, choices=GENRE_CHOICES, max_length=50)
    copyright_info = models.CharField(blank=False, max_length=200)
    production_info = models.CharField(blank=False, max_length=200)
    track_explicit_lyrics = models.BooleanField(default=False)
    origin_country = models.CharField(blank=False, choices=COUNTRY_CODES_CHOICES, max_length=5)
    track_lyricist = models.CharField(blank=False, max_length=200)
    track_composer = models.CharField(blank=False, max_length=200)
    track_arranger = models.CharField(blank=True, max_length=200)
    track_producer = models.CharField(blank=True, max_length=200)
    track_publisher = models.CharField(blank=False, max_length=200)
    ISRC = models.CharField(blank=True, max_length=200)
    musical_work_rights = models.CharField(blank=False, max_length=200)
    music_percentage = models.SmallIntegerField(default=100)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.SET_NULL, blank=True, null=True)
    submitter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(editable=False, blank=True)
    date_modified = models.DateTimeField(blank=True)

    def __str__(self):
        return self.track_title

    def save(self, *args, **kwargs):
        # set the key so that it's incremental on a per-user basis
        key = cal_key(self.submitter)
        self.key = key
        # update timestamps
        if not self.id:
            self.date_created = timezone.now()
        self.date_modified = timezone.now()
        super().save(*args, **kwargs)

def cal_key(submitter):
    present_keys = Track.objects.filter(submitter=submitter).order_by('-key').values_list('key', flat=True)
    if present_keys:
        return present_keys[0] + 1
    else:
        return 1
