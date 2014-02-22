from django.db import models


class Member(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    active_member = models.BooleanField(default=False)
    amount_payed = models.FloatField(default=0)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
