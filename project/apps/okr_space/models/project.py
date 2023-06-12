from .base import BaseModel
from django.db import models

class ProjectModel(BaseModel):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    
    class Meta:
        db_table = 'project'

class Employee(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee'

class Goal(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'goal'

class Bonus(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    star_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'bonus'