# import pytest
from django.test import Client
from django.urls import reverse, resolve


def test_urllist_view():
    client = Client()
    response = client.get('/wordcounter/')
    assert response.status_code == 200


def test_urllist_url():
    path = reverse('wordcounter')
    assert resolve(path).view_name == "wordcounter"
