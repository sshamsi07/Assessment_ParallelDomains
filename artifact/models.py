from django.db import models
import uuid


# Create your models here.
class Artifact(models.Model):

    slug = models.SlugField(db_index=True, max_length=30, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255)
    PLATFORM_CHOICES = (('Linux', 'Linux'), ('Windows', 'Windows'))
    platform_used = models.CharField(max_length=10, choices=PLATFORM_CHOICES)

    def __str__(self):
        return self.slug