from django.conf import settings
from django.db import models

# Create your models here.
class Version(models.Model):
    versions = models.CharField(max_length=15)

    def __str__(self):
        return self.versions