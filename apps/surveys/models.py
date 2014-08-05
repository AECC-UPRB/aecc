from django.db import models
from autoslug import AutoSlugField


class Survey(models.Model):
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
    choices = models.CharField(max_length=140)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choices
