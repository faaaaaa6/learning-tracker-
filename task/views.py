from rest_framework import generics #  bring the prebuild tools from Drf to handle request
from rest_framework.permissions import IsAuthenticated
from .models import Task #for fetch the data from the database
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


#used this task for (create(POST)/read(GET)) for the user
class TaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# used this task for (update(PUT)/delete(DELETE))
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class progressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        tasks = Task.objects.filter(user=request.user)
        total = tasks.count()
        completed = tasks.filter(is_completed=True).count()
        pending = total - completed
        percentage = (completed/total*100)if total > 0 else 0

        return Response({
            "total_tasks" : total,
            "completed_tasks":completed,
            "pending_tasks": pending,
            "completion_percentage":round(percentage,1),
        })
    