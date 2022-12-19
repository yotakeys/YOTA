from django.urls import reverse, resolve
from main.views import homeView
import pytest
from django.test import RequestFactory


@pytest.mark.django_db
def test_main_view():
    path = reverse("home")
    request = RequestFactory().get(path)
    response = homeView(request)
    assert response.status_code == 200


def test_main_url():
    path = reverse('home')
    print(path)
    assert resolve(path).view_name == "home"
