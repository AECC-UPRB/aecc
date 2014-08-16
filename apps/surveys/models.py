from django.db import models
from autoslug import AutoSlugField
from django.conf import settings


class Survey(models.Model):
    sent_by = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = AutoSlugField(populate_from='title')
    is_closed = models.BooleanField(default=False)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.title


class Poll(models.Model):
    survey = models.ForeignKey(Survey)
    question = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=140, blank=False)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
