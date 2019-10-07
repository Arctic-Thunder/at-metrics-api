from django.contrib import admin

# Register your models here.
from .models import Metric

admin.site.register(Metric)