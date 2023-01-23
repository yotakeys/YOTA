from django.urls import path
from .views import testIndexBlog

urlpatterns = [
    path('', name='blog', view=testIndexBlog),
]