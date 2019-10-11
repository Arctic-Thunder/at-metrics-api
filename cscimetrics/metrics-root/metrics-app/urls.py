from django.urls import path, include
from.views import ProjectList, ProjectDetail, MetricList, MetricDetail, UserCreate
from rest_framework.authtoken import views

app_name = "metrics"

urlpatterns = [
    path('projects/', ProjectList.as_view()),
    path('projects/<int:project_id>', ProjectDetail.as_view()),
    path('projects/<int:project_id>/metric/<int:metric_id>', MetricDetail.as_view()),
    path('users/', UserCreate.as_view(), name="user_create"),
    path("login/", views.obtain_auth_token, name="login"),
]