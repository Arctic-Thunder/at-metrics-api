from django.db import models


# Create your models here.
class Metric(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=20)
    data = models.TextField()

    def __str__(self):
        return self.name + ' ' + str(self.timestamp)
