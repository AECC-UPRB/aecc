from time import time

from django.db import models
from autoslug import AutoSlugField


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class Event(models.Model):
    MONTH_CHOICES = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    month = models.CharField(max_length=10, choices=MONTH_CHOICES)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    promo_picture = models.FileField(upload_to=get_upload_file_name, blank=True)
    title_slug = AutoSlugField(populate_from='title', unique=True)
    month_slug = AutoSlugField(populate_from='month', unique=True)

    def __unicode__(self):
        return self.title
