from django.db import models

class ViewCount(models.Model):
    count = models.IntegerField(default=0)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

