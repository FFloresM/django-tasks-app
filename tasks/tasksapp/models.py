from enum import _auto_null, auto
from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=200)
    day = models.DateTimeField(auto_now=False)
    reminder = models.BooleanField()

    def __str__(self) -> str:
        return self.text