from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    about = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
