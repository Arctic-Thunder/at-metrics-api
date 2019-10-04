from django.db import models


# Create your models here.
class Metric(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=120)
    description = models.TextField()
    type = models.ForeignKey('MetricType', on_delete='PROTECT')

    def __str__(self):
        return self.name + ' ' + str(self.timestamp)


class MetricType(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.name
