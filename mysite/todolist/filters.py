
from django_filters import FilterSet
from .models import Task

class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {
            'completed': ['exact']

        }