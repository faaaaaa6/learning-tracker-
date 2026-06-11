from django.urls import path
from .views import TaskList,TaskDetail

urlpatterns = [
    path("tasks/",TaskList.as_view(), name='tasks'),
    #<in:pk>/ uses for retrieve the specific object in database ,pk =primary key
    path('tasks/<int:pk>/',TaskDetail.as_view(), name='task-detail'),
]
