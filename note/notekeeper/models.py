from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_creation = models.DateTimeField('date created', default=timezone.now())
    date_update = models.DateTimeField('date updated', default=timezone.now())

    def __str__(self):
        return "ID: {} \nTitle: {} \nContent: {} \nDate of Creation: {} \nDate of update: {}".format(self.id, self.title, self.content, self.date_creation, self.date_update)