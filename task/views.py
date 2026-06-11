from rest_framework import generics# for bring the prebuild tools from Drf
from rest_framework.permissions import IsAuthenticated
from .models import Task #for fetch the data from the database
from .serializers import TaskSerializer

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
    serilaizer_class = TaskSerializer

    def get_queryset(self):
        return Task>object.filter(user=self.request.user)
        