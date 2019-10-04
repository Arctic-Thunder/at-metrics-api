from rest_framework import generics
from rest_framework.response import Response

from .models import Metric, MetricType
from .serializers import MetricSerializer, MetricTypeSerializer, UserSerializer


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


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

# class LoginView(views.APIView):
#     permission_classes = ()
#
#     def post(self, request):
#         uname = request.data.get('username')
#         passwd = request.data.get('password')
#         user = authenticate(username=uname, password=passwd)
#         if user:
#             return Response({"token": user.auth_token_key})
#         else:
#             return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
