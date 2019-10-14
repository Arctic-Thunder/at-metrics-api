from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField



# Create your models here.

# Represents a user's project
DEFAULT_OWNER_ID = 1
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=DEFAULT_OWNER_ID
    )

    def __str__(self):
        return self.name


# Represents a project's metric
class Metric(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = JSONField()

    project_id = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_id) + '-' + str(self.id) + '-' + str(self.timestamp)
