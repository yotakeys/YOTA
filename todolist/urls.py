from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('create/', TaskCreate.as_view(), name='taskcreate'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='taskupdate'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='taskdelete'),
]
