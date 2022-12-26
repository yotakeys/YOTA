from django.urls import path
from .views import UrlList, redirectUrl, UpdateUrl, DeleteUrl, CreateUrl

urlpatterns = [
    path('', name='url', view=UrlList.as_view()),
    path('update/<str:pk>/', name="urlUpdate", view=UpdateUrl.as_view()),
    path('delete/<str:pk>/', name="urlDelete", view=DeleteUrl.as_view()),
    path('create/', name="urlCreate", view=CreateUrl.as_view()),
    path('<str:shortUrl>/', name='urlRedirect', view=redirectUrl),
]
