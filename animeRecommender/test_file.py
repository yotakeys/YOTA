# import pytest
from django.test import Client
from django.urls import reverse, resolve


def test_animerecommender_view():
    client = Client()
    response = client.get('/animerecommender/')
    assert response.status_code == 200


def test_animerecommender_url():
    path = reverse('animerecommender')
    assert resolve(path).view_name == "animerecommender"
