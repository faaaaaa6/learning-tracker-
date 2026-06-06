from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    


