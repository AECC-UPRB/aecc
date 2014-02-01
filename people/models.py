from time import time

from django.db import models


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class People(models.Model):
    PRESIDENT = 'PR'
    VICEPRESIDENT = 'VP'
    TREASURER = 'TR'
    SECRETARY = 'SE'
    VOCAL = 'VO'
    POSITION_OPTIONS = (
        (PRESIDENT, 'President'),
        (VICEPRESIDENT, 'Vice-President'),
        (TREASURER, 'Treasurer'),
        (SECRETARY, 'Secretary'),
        (VOCAL, 'Vocal'),
    )
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    position = models.CharField(max_length=2, choices=POSITION_OPTIONS)
    picture = models.FileField(upload_to=get_upload_file_name)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.lastname)
