from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import TaskFilter



class TaskViewSet(viewsets.ModelViewSet):
     queryset = Task.objects.all()
     serializer_class = TaskSerializer
     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
     filterset_class = TaskFilter
     search_fields = ['title']
     ordering_fields = ['created_date', ]