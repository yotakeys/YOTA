from django.urls import path
from .views import wordCounter

urlpatterns = [
    path('', wordCounter, name='wordcounter'),
]
