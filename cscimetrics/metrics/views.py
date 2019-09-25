from rest_framework import generics

from .models import Metric, MetricType
from .serializers import MetricSerializer, MetricTypeSerializer


# Create your views here.


class MetricList(generics.ListCreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer


class MetricDetail(generics.RetrieveDestroyAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer


class MetricTypeList(generics.ListCreateAPIView):
    queryset = MetricType.objects.all()
    serializer_class = MetricTypeSerializer
