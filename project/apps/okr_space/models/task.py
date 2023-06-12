from .base import BaseModel
from django.db import models
from django.contrib.auth.models import User

class TaskModel(BaseModel):
    project = models.ForeignKey('ProjectModel', on_delete=models.CASCADE, related_name='releted_tasks')
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta:
        db_table = 'task'

class TaskMemberModel(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='releted_tasks')
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE, related_name='releted_members')

    class Meta:
        db_table = 'task_member'