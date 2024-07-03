import django_filters
from tasky.models import Task

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status']
