"""Models for the movie application"""
from django.db import models


class Movie(models.Model):
    """Movies Classes"""
    title = models.CharField(max_length=20, blank=False)
    poster = models.ImageField(upload_to ="upload/poster/", blank=False)
    genre = models.CharField(max_length=20, blank=False)
    actor = models.CharField(max_length=20, blank=False)
    description = models.TextField(blank=False)
    year = models.IntegerField(blank=False)

    objects = models.Manager()

    def __str__(self):
        return self.title
