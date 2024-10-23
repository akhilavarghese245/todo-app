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
