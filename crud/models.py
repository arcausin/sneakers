from msilib.schema import Class
from time import timezone

from django.db import models

from datetime import datetime
# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField('date')

    def __str__(self):
        return self.text

    def publier(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)