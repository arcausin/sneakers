from msilib.schema import Class

from django.db import models

# Create your models here.

class Produit(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name