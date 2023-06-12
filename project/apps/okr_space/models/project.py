from .base import BaseModel
from django.db import models
from django.contrib.auth.models import User

class ProjectModel(BaseModel):
    name = models.CharField(max_length=255)
    custo = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    gerente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gerente')
    
    class Meta:
        db_table = 'project'
