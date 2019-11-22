from django.db import models
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):
    title = models.CharField(_('title'), unique=False, max_length=120, null=False)

    class Meta:
        ordering = ['title']


class Reader(models.Model):
    name = models.CharField(_('name'), unique=True, max_length=120, null=False)
    books = models.ManyToManyField(Book)
