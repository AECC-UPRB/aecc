from django.db import models
from autoslug import AutoSlugField
from django.conf import settings


class Survey(models.Model):
    sent_by = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')

    def __unicode__(self):
        return self.title


class Poll(models.Model):
    survey = models.ForeignKey(Survey)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choices = models.CharField(max_length=140, blank=False)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choices
