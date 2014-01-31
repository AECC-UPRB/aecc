from time import time

from django.db import models


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)


class Events(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    month = models.CharField(max_length=12)
    event_date = models.DateTimeField('published date')
    location = models.CharField(max_length=100)
    promo_picture = models.FileField(upload_to=get_upload_file_name)

    def __unicode__(self):
        return self.tittle
