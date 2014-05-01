from django.db import models

from autoslug import AutoSlugField


class Article(models.Model):
    BRANCH_CHOICES = (
        ('directive', 'Directive'),
        ('starting_up', 'Starting_up'),
        ('devteam', 'Devteam'),
    )

    created_by = models.ForeignKey('users.User')
    title = models.CharField(unique=True, max_length=25)
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=12)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=False)
    article_slug = AutoSlugField(populate_from='title')
    branch_slug = AutoSlugField(populate_from='branch')

    def __unicode__(self):
        return self.title
