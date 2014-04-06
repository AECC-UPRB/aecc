from django.db import models

from autoslug import AutoSlugField


class Article(models.Model):
    DIRECTIVE = 'directive'
    STARTING_UP = 'starting_up'
    DEVTEAM = 'devteam'
    BRANCH_CHOICES = (
        (DIRECTIVE, 'Directive'),
        (STARTING_UP, 'Starting_up'),
        (DEVTEAM, 'Devteam'),
    )

    user = models.ForeignKey('people.People')
    title = models.CharField(unique=True, max_length=25)
    description = models.TextField(max_length=500)
    date = models.DateField()
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=12)
    article_slug = AutoSlugField(populate_from='title')
    branch_slug = AutoSlugField(populate_from='branch')
