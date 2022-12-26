from django.test import Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
import pytest
from .models import Url


@pytest.mark.django_db  # give test access to database
def test_create_url():
    # Create dummy data
    url = Url.objects.create(
        longUrl="Dump", shortUrl="dumptesting",)
    # Assert the dummy data saved as expected
    assert url.longUrl == "Dump"
    assert url.shortUrl == "dumptesting"


@pytest.mark.django_db
def test_urllist_view():
    user = User.objects.create(username='testuser')
    user.set_password('12345')
    user.save()
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/url/')
    assert response.status_code == 200


def test_urllist_url():
    path = reverse('url')
    print(path)
    assert resolve(path).view_name == "url"


@pytest.mark.django_db
def test_urlcreate_view():
    user = User.objects.create(username='testuser')
    user.set_password('12345')
    user.save()
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/url/create/')
    assert response.status_code == 200


def test_urlcreate_url():
    path = reverse('urlCreate')
    print(path)
    assert resolve(path).view_name == "urlCreate"


@pytest.mark.django_db
def test_urlupdateview():
    users = User.objects.create(username='testuser')
    users.set_password('12345')
    users.save()
    Url.objects.create(user=users, longUrl="dumpbos", shortUrl="dump")
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/url/update/dump/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_urldeleteview():
    users = User.objects.create(username='testuser')
    users.set_password('12345')
    users.save()
    Url.objects.create(user=users, longUrl="dumpbos", shortUrl="dump")
    client = Client()
    client.login(username='testuser', password='12345')
    response = client.get('/url/delete/dump/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_urlredirect():
    Url.objects.create(longUrl="https://github.com/yotakeys", shortUrl="dump")
    client = Client()
    response = client.get('/url/dump/')
    assert response.status_code == 302