from django.urls import path
from .views import animeRecommender

urlpatterns = [
    path('', animeRecommender, name='animerecommender'),
]
