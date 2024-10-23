from django.urls import path
from .views import TaskAPIView

urlpatterns = [
    path('api/add_task/', TaskAPIView.as_view(), name='add_task')
]