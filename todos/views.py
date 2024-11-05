from functools import partial

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status
from .models import Task


class TaskAPIView(APIView):


    def post(self, request):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Task added successfully', 'data': request.data},status=status.HTTP_200_OK)  # Created status code
        except Exception as e:
            return Response({'message': 'Error in adding task','data':{}}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        task_id = request.data.get('task_id')
        task_info = Task.objects.filter(task_id=task_id).first()
        title = request.data.get('title')
        description = request.data.get('description')
        is_done = request.data.get('is_done')

        data = {'title': title, 'description': description, 'is_done': is_done}
        task_serializer = TaskSerializer(instance=task_info, data=data, partial=True)
        if task_serializer.is_valid():
            task_serializer.update(task_info, validated_data = data)
            return Response({'message': 'task updated successfully', 'data':request.data}, status=status.HTTP_200_OK)
        return Response({'message': 'Error in adding task', 'data': {}}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        task_id = request.data.get('task_id')
        try:
            task_info = Task.objects.get(task_id=task_id)
            task_info.delete()
            return Response({'message': 'Task deleted successfully', 'data':{}}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': 'Task not found', 'data':{}}, status=status.HTTP_404_NOT_FOUND)

class TaskListView(APIView):
    def get(self, request):
        try:
            task_info = Task.objects.filter(is_done=False)
            serializer = TaskSerializer(task_info, many=True)
            return Response({'message': 'Tasks not done is fetched', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'tasks cannot be fetched', 'data': {}}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        try:
            task_id = request.data.get('task_id')
            is_done = request.data.get('is_done')
            task_info = Task.objects.get(task_id=task_id)
            data = {'is_done': is_done}
            task_serializer = TaskSerializer(instance=task_info, data=data, partial=True)
            if task_serializer.is_valid():
                task_serializer.update(task_info, validated_data = data)
                return Response({'message': 'Task marked done successfully', 'data':request.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'tasks cannot be fetched', 'data': {}}, status=status.HTTP_404_NOT_FOUND)

