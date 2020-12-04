from django.db import models
from django.db.models.fields import CharField


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    full_description = models.TextField(blank=True)
    image_main = models.ImageField(upload_to='portfolio/images/')
    image_1 = models.ImageField(upload_to='portfolio/images/', blank=True)
    image_2 = models.ImageField(upload_to='portfolio/images/', blank=True)
    image_3 = models.ImageField(upload_to='portfolio/images/', blank=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    tech = models.TextField(blank=True)

    def __str__(self):
        return self.title

