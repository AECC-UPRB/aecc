from django.db import models

from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from .constants import BRANCH_CHOICES


class Article(models.Model):
    class Meta:
        ordering = ['-created_at']

    created_by = models.ForeignKey('users.User')
    title = models.CharField(unique=True, max_length=25)
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=12)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now=False)
    is_published = models.BooleanField(default=False)
    article_slug = AutoSlugField(populate_from='title')
    branch_slug = AutoSlugField(populate_from='branch')

    tags = TaggableManager()

    def __unicode__(self):
        return self.title
