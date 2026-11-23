import json
from http import HTTPStatus

from api import models
from django.test import Client, TestCase


class TaskiAPITestCase(TestCase):
  def setUp(self):
    self.guest_client = Client()

  def test_list_exists(self):
    """Проверка доступности и формата списка задач."""
    response = self.guest_client.get('/api/tasks/')

    self.assertEqual(response.status_code, HTTPStatus.OK)
    self.assertEqual(response['Content-Type'], 'application/json')
    self.assertIsInstance(response.json(), list)

  def test_task_creation(self):
    """Проверка создания задачи."""
    data = {'title': 'Test', 'description': 'Test'}
    response = self.guest_client.post('/api/tasks/', data=data)
    self.assertEqual(response.status_code, HTTPStatus.CREATED)
    self.assertTrue(models.Task.objects.filter(title='Test').exists())

  def test_task_creation_without_title(self):
    """Проверка создания задачи без заголовка."""
    data = {'description': 'Test description'}

    response = self.guest_client.post('/api/tasks/', data=data)

    self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
    self.assertFalse(models.Task.objects.exists())

  def test_task_update(self):
    """Проверка редактирования задачи."""
    task = models.Task.objects.create(
      title='Old title',
      description='Old description'
    )

    data = {
      'title': 'New title',
      'description': 'New description',
      'completed': True
    }

    response = self.guest_client.put(
      f'/api/tasks/{task.id}/',
      data=json.dumps(data),
      content_type='application/json'
    )

    self.assertEqual(response.status_code, HTTPStatus.OK)

    task.refresh_from_db()
    self.assertEqual(task.title, 'New title')
    self.assertEqual(task.description, 'New description')
    self.assertTrue(task.completed)

  def test_task_delete(self):
    """Проверка удаления задачи."""
    task = models.Task.objects.create(
      title='Task to delete',
      description='Test'
    )

    response = self.guest_client.delete(f'/api/tasks/{task.id}/')

    self.assertEqual(response.status_code, HTTPStatus.OK)
    self.assertFalse(models.Task.objects.filter(id=task.id).exists())

  def test_task_str(self):
    """Проверка строкового представления задачи."""
    task = models.Task(title='My task', description='Test')
    self.assertEqual(str(task), 'My task')
