from rest_framework import generics
from rest_framework.response import Response

from .models import Metric
from .serializers import MetricSerializer, UserSerializer

class MetricList(generics.ListCreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer


class MetricDetail(generics.RetrieveDestroyAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
