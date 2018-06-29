from django.db import models

# Create your models here.


class FileUploat(models.Model):
    name = models.FileField()

    def __str__(self):
        return self.name.name



