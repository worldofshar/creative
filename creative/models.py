from django.db import models

# Create your models here.


class Repository(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(default="short", max_length=15)
    status = models.CharField(default="draft", max_length=15)
    content = models.TextField(max_length=100000)

    def __str__(self):
        return self.name
