from django.urls import path
from .views import TaskAPIView, TaskListView

urlpatterns = [
    path('api/add_task/', TaskAPIView.as_view(), name='add_task'),
    path('api/list_tasks/', TaskListView.as_view(), name='list_tasks')
]