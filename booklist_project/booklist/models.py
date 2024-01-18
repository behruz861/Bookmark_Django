from django.db import models
from autoslug import AutoSlugField
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, populate_from='title')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year_published = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    rating = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 11)])
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title