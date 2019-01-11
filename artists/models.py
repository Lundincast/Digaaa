from django.db import models
from django.utils import timezone

from users.models import User
from common.models import COUNTRY_CODES_CHOICES, LANGUAGE_CODES_CHOICES


class Artist(models.Model):
    key = models.PositiveIntegerField(editable=False, blank=True)
    artist_name = models.CharField(max_length=200)
    label_name = models.CharField(max_length=200)
    artist_website = models.URLField(blank=True, null=True)
    distribution_territory = models.CharField(blank=False, choices=COUNTRY_CODES_CHOICES, max_length=10, default='ww')
    dont_deliver_shop = models.CharField(max_length=200, blank=True, null=True)
    only_deliver_shop = models.CharField(max_length=200, blank=True, null=True)
    allow_subscription = models.BooleanField(default=True)
    albums_language = models.CharField(max_length=3, choices=LANGUAGE_CODES_CHOICES, default='en')
    copyright_info = models.CharField(max_length=200)
    production_info = models.CharField(max_length=200)
    origin_country = models.CharField(blank=False, choices=COUNTRY_CODES_CHOICES, max_length=10, default='ww')
    lyricist = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    arranger = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    musical_work_rights = models.CharField(max_length=200)
    submitter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    date_created = models.DateTimeField(editable=False, blank=True)
    date_modified = models.DateTimeField(blank=True)

    def __str__(self):
        return self.artist_name

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
    present_keys = Artist.objects.filter(submitter=submitter).order_by('-key').values_list('key', flat=True)
    if present_keys:
        return present_keys[0] + 1
    else:
        return 1