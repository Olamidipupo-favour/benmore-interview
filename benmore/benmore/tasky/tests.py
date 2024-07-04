from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group
from benmore.tasky.serializers import UserSerializer, GroupSerializer, TaskSerializer, RegisterSerializer
from tasky.models import Task
from benmore.tasky.views import UserViewSet, GroupViewSet, TaskViewSet, RegisterView, CheckAuthView

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwOTk5ODIwLCJpYXQiOjE3MjAxMzU4MjAsImp0aSI6ImM4MzM0ODZmMDA1YzQyODk4YmY5NTBjODcxNmJkYjNlIiwidXNlcl9pZCI6M30.00uT41AzFlUfFES01K-zQxRgiq-UWnw_yUa5ULKyxZA"

class TestUserViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_detail(self):
        url = reverse('user-detail', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_create(self):
        url = reverse('user-list')
        data = {'username': 'newuser', 'password': 'newpassword123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_update(self):
        url = reverse('user-detail', args=[self.user.pk])
        data = {'username': 'updateduser'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_user_delete(self):
        url = reverse('user-detail', args=[self.user.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())

class TestTaskViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.task = Task.objects.create(title='Test Task', description='Task description', assigned_to=self.user)

    def test_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_detail(self):
        url = reverse('task-detail', args=[self.task.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_create(self):
        url = reverse('task-list')
        data = {
            "title": "Complete Project Proposal",
            "description": "Write and finalize the project proposal document.",
            "priority": "High",
            "category": "Planning",
            "due_date": "2024-07-31T12:00:00Z",
            "status": "In Progress",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Task.objects.filter(title='Complete Project Proposal').exists())

    def test_task_update(self):
        url = reverse('task-detail', args=[self.task.pk])
        data = {'title': 'Updated Task'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_task_delete(self):
        url = reverse('task-detail', args=[self.task.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

class TestRegisterView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        url = reverse('register')
        data = {'username': 'newuser', 'password': 'newpassword123', 'email': 'newuser@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())

class TestCheckAuthView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_check_authentication(self):
        url = reverse('check-auth')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['is_authenticated'])
