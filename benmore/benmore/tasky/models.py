from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    status= models.CharField(max_length=50, choices=[('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Overdue', 'Overdue')])
    category = models.CharField(max_length=50)
    due_date = models.TimeField()

    def __str__(self):
        return self.title