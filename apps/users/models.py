from time import time

from django.db import models


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class User(models.Model):
    PRESIDENT = 'PR'
    VICEPRESIDENT = 'VP'
    TREASURER = 'TR'
    SECRETARY = 'SE'
    VOCAL = 'VO'
    MEMBER = 'ME'
    POSITION_OPTIONS = (
        (PRESIDENT, 'President'),
        (VICEPRESIDENT, 'Vice-President'),
        (TREASURER, 'Treasurer'),
        (SECRETARY, 'Secretary'),
        (VOCAL, 'Vocal'),
        (MEMBER, 'Member'),
    )
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    student_number = models.CharField(max_length=9, unique=True)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              default='M')
    active_member = models.BooleanField(default=False)
    amount_payed = models.FloatField(default=0)
    position = models.CharField(max_length=2, choices=POSITION_OPTIONS,
                                default='ME')
    picture = models.FileField(upload_to=get_upload_file_name)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
