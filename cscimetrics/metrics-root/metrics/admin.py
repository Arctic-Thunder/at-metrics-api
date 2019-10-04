from django.contrib import admin

# Register your models here.
from .models import Metric, MetricType

admin.site.register(Metric)
admin.site.register(MetricType)