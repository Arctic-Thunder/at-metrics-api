from django.urls import path
from.views import MetricList, MetricDetail, MetricTypeList
from rest_framework.documentation import include_docs_urls

app_name = "metrics"

urlpatterns = [
    path('metrics/', MetricList.as_view()),
    path('metrics/<int:pk>', MetricDetail.as_view()),
    path('metrics/types/', MetricTypeList.as_view()),
]