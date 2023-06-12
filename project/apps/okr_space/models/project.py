from .base import BaseModel
from django.db import models

class ProjectModel(BaseModel):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    
    class Meta:
        db_table = 'project'
