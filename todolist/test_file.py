from django.test import Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
import pytest
from .models import Task


@pytest.mark.django_db  # give test access to database
def test_create_task():
    # Create dummy data
    task = Task.objects.create(
        title="Dump", description="dump testing",)
    # Assert the dummy data saved as expected
    assert task.title == "Dump"
    assert task.description == "dump testing"


@pytest.mark.django_db
def test_tasklist_view():
    user = User.objects.create(username='testuser')
    user.set_password('12345')
    user.save()
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/todo/')
    assert response.status_code == 200


def test_tasklist_url():
    path = reverse('tasks')
    print(path)
    assert resolve(path).view_name == "tasks"


@pytest.mark.django_db
def test_taskcreate_view():
    user = User.objects.create(username='testuser')
    user.set_password('12345')
    user.save()
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/todo/taskcreate/')
    assert response.status_code == 200


def test_taskcreate_url():
    path = reverse('taskcreate')
    print(path)
    assert resolve(path).view_name == "taskcreate"


@pytest.mark.django_db
def test_taskupdateview():
    users = User.objects.create(username='testuser')
    users.set_password('12345')
    users.save()
    Task.objects.create(id=0, user=users, title='test', description='test')
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/todo/taskupdate/0/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_taskdeleteview():
    users = User.objects.create(username='testuser')
    users.set_password('12345')
    users.save()
    Task.objects.create(id=0, user=users, title='test', description='test')
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/todo/taskdelete/0/')
    assert response.status_code == 200
