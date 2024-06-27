from django.db import models
from django.utils import timezone
from datetime import timedelta


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField()
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='posts')

    def __str__(self):
        return self.title

    def published_recently(self):
        return self.published_date >= timezone.now() - timedelta(days=7)

    published_recently.boolean = True
    published_recently.short_description = 'Published Recently?'