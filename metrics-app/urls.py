from django.urls import path, include
# from.views import ProjectViewSet, ProjectDetail, MetricViewSet, MetricDetail, UserCreate
from .views import ProjectViewSet, MetricViewSet, UserCreate
from rest_framework.authtoken import views
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework.routers import DefaultRouter

app_name = "metrics"

extRouter = ExtendedSimpleRouter()
(
    extRouter.register(r'projects', ProjectViewSet, basename='project')
    .register(r'metrics', MetricViewSet, basename='projects-metric', parents_query_lookups=['project__metrics'])
)

defRouter = DefaultRouter()
(
    defRouter.register(r'new_user', UserCreate, basename='new-user')
)

urlpatterns = [
    path('', include(extRouter.urls)),
    path('', include(defRouter.urls)),
    path('login/', views.obtain_auth_token, name="login")
]