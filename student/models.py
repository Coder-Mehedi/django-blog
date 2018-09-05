from django.db import models

class StudentResult(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=125)
    result = models.CharField(max_length=25)

    def __str__(self):
        return self.name
