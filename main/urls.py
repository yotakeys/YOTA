from django.urls import path
from .views import homeView

urlpatterns = [
    path('', view=homeView, name='home'),
]
