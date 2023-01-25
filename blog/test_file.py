from django.test import Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
import pytest
from .models import Post


@pytest.mark.django_db  # give test access to database
def test_create_post():
    # Create dummy data
    user = User.objects.create(username='testuser')
    user.set_password('12345')
    user.save()
    post = Post.objects.create(
        title="dump 1", content="dump testing", author=user, slug="dump-1")
    # Assert the dummy data saved as expected
    assert post.title == "dump 1"
    assert post.content == "dump testing"
    assert post.slug == "dump-1"
    assert post.author == user


@pytest.mark.django_db
def test_postlist_view():
    client = Client()
    response = client.get('/blog/')
    assert response.status_code == 200


def test_postlist_url():
    path = reverse('blog')
    assert resolve(path).view_name == "blog"


@pytest.mark.django_db
def test_postdetail_view():
    user = User.objects.create(username='testuser')
    user.set_password('12345')
    user.save()
    Post.objects.create(
        title="dump 1", content="dump testing", author=user, slug="dump-1")
    client = Client()
    response = client.get('/blog/dump-1/')
    assert response.status_code == 200
