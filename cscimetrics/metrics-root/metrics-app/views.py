from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Project, Metric
from .serializers import ProjectSerializer, MetricSerializer, UserSerializer


class ProjectViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class ProjectDetail(NestedViewSetMixin, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProjectSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return Project.objects.filter(owner=user)


class MetricViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = MetricSerializer

    def get_queryset(self):
        user = self.request.user
        id = self.request.path.split('/')
<<<<<<< HEAD
        return Metric.objects.filter(project_id=path[3]).filter(project_id__owner=user)
=======
        return Metric.objects.filter(project_id__owner=user).filter(project_id=id[3])
>>>>>>> 956aba3ca4835c7d4c7bec64f48aeb7446142f55

    def perform_create(self, serializer):
        id = self.request.path.split('/')
        project = Project.objects.get(pk=id[3])
        if project:
            serializer.save(project_id=project)


# class MetricDetail(NestedViewSetMixin,generics.RetrieveDestroyAPIView):
#     serializer_class = MetricSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return Metric.objects.filter(project_id__owner=user)


class UserCreate(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
