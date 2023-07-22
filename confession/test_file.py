from django.test import Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
import pytest
from .models import Confession


@pytest.mark.django_db  # give test access to database
def test_create_confession():
    # Create dummy data
    confess = Confession.objects.create(
        slug="test-confess", title="test-title",
        sender="test", target="test", message="test")
    # Assert the dummy data saved as expected
    assert confess.slug == "test-confess"
    assert confess.title == "test-title"
    assert confess.sender == "test"
    assert confess.target == "test"
    assert confess.message == "test"


@pytest.mark.django_db
def test_confessionlist_view():
    user = User.objects.create(username='testuser')
    user.set_password('12345')
    user.save()
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/confession/')
    assert response.status_code == 200


def test_confessionlist_url():
    path = reverse('confessionList')
    assert resolve(path).view_name == "confessionList"


@pytest.mark.django_db
def test_confessioncreate_view():
    user = User.objects.create(username='testuser')
    user.set_password('12345')
    user.save()
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/confession/create/')
    assert response.status_code == 200


def test_confessioncreate_url():
    path = reverse('confessionCreate')
    assert resolve(path).view_name == "confessionCreate"


@pytest.mark.django_db
def test_urlupdateview():
    users = User.objects.create(username='testuser')
    users.set_password('12345')
    users.save()
    Confession.objects.create(user=users, slug="test-confess", title="test-title",
                              sender="test", target="test", message="test")
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/confession/update/test-confess/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_confessiondeleteview():
    users = User.objects.create(username='testuser')
    users.set_password('12345')
    users.save()
    Confession.objects.create(user=users, slug="test-confess", title="test-title",
                              sender="test", target="test", message="test")
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/confession/delete/test-confess/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_confessionredirect():
    users = User.objects.create(username='testuser')
    users.set_password('12345')
    users.save()
    Confession.objects.create(user=users, slug="test-confess", title="test-title",
                              sender="test", target="test", message="test")
    client = Client()
    response = client.get('/confession/test-confess/')
    assert response.status_code == 200
