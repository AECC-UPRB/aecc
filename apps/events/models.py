from time import time

from django.db import models
from django.core.urlresolvers import reverse_lazy

from autoslug import AutoSlugField
from taggit.managers import TaggableManager

from .constants import MONTH_CHOICES


def get_upload_file_name(instance, filename):
    return "static/uploaded_files/%s_%s" % \
        (str(time()).replace('.', '_'), filename)


class Event(models.Model):
    class Meta:
        ordering = ['-event_date']

    title = models.CharField(max_length=100)
    description = models.TextField()
    month = models.CharField(max_length=10, choices=MONTH_CHOICES)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    promo_picture = models.FileField(upload_to=get_upload_file_name, blank=True)
    title_slug = AutoSlugField(populate_from='title', unique=True)
    month_slug = AutoSlugField(populate_from='month', unique=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('events:event',
                            args=[self.month, self.title_slug])
