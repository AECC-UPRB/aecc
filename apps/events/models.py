from time import time

from django.db import models
from autoslug import AutoSlugField


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class Events(models.Model):
    JANUARY = 'january'
    FEBRUARY = 'february'
    MARCH = 'march'
    APRIL = 'april'
    MAY = 'may'
    JUNE = 'june'
    JULY = 'july'
    AUGUST = 'august'
    SEPTEMBER = 'september'
    OCTOBER = 'october'
    NOVEMBER = 'november'
    DECEMBER = 'december'
    MONTH_CHOICES = (
        (JANUARY, 'January'),
        (FEBRUARY, 'February'),
        (MARCH, 'March'),
        (APRIL, 'April'),
        (MAY, 'May'),
        (JUNE, 'June'),
        (JULY, 'July'),
        (AUGUST, 'August'),
        (SEPTEMBER, 'September'),
        (OCTOBER, 'October'),
        (NOVEMBER, 'November'),
        (DECEMBER, 'December'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    month = models.CharField(max_length=10, choices=MONTH_CHOICES)
    event_date = models.DateTimeField('published date')
    location = models.CharField(max_length=100)
    promo_picture = models.FileField(upload_to=get_upload_file_name, blank=True)
    title_slug = AutoSlugField(populate_from='title', unique=True)
    month_slug = AutoSlugField(populate_from='month', unique=True)


    def __unicode__(self):
        return self.title
