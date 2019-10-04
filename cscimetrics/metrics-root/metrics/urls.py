from django.urls import path, include
from.views import MetricList, MetricDetail, MetricTypeList, UserCreate
from rest_framework.authtoken import views

app_name = "metrics"

urlpatterns = [
    path('metrics/', MetricList.as_view()),
    path('metrics/<int:pk>', MetricDetail.as_view()),
    path('metrics/types/', MetricTypeList.as_view()),
    path('users/', UserCreate.as_view(), name="user_create"),
    path("login/", views.obtain_auth_token, name="login"),
]