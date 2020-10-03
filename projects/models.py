from django.db import models


# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.summary
