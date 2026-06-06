from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:# configuration box
        model = Task
        fields = ['id','title','is_completed','data']
        read_only_fields = ['date']
        
