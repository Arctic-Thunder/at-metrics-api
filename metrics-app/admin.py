from django.contrib import admin

# Register your models here.
from .models import Project, Metric

admin.site.register(Project)
admin.site.register(Metric)