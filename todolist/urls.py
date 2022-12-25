from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [   
    path('', TaskList.as_view(), name='tasks'),
    path('taskcreate/', TaskCreate.as_view(), name='taskcreate'),
    path('taskupdate/<int:pk>/', TaskUpdate.as_view(), name='taskupdate'),
    path('taskdelete/<int:pk>/', TaskDelete.as_view(), name='taskdelete'),
]
