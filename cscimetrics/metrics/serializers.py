from rest_framework import serializers

from .models import Metric, MetricType


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'
        read_only_fields = ['id', 'timestamp']

class MetricTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricType
        fields = '__all__'