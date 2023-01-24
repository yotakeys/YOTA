from .views import PostList, PostDetail
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('<slug:slug>/', PostDetail.as_view(), name='postDetail'),
]