from django.db import models

# Create your models here.
from django.db import models


class UserHistory(models.Model):

    history_text = models.TextField(max_length=500)

    def __str__(self):
        return self.history_text
