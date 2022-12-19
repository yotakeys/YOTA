import pytest
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import RequestFactory, Client
from User.views import Login, Register


@pytest.mark.django_db  # give test access to database
def test_register_user():
    # Create dummy data
    contact = User.objects.create(
        username="Dump", password="75859538350",)
    # Assert the dummy data saved as expected
    assert contact.username == "Dump"
    assert contact.password == "75859538350"


@pytest.mark.django_db
def test_login_view():
    client = Client()
    response = client.get('/user/login/')
    # assert status code from requesting the view is 200(OK success status response code)
    assert response.status_code == 200


def test_login_url():
    path = reverse('login')
    print(path)
    assert resolve(path).view_name == "login"


@pytest.mark.django_db
def test_register_view():
    client = Client()
    response = client.get('/user/register/')
    # assert status code from requesting the view is 200(OK success status response code)
    assert response.status_code == 200


def test_register_url():
    path = reverse('register')
    print(path)
    assert resolve(path).view_name == "register"
