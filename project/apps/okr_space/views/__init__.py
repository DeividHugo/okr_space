from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from models.task import TaskModel


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"


class Home(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class Project(LoginRequiredMixin, TemplateView):
    template_name = "project.html"

class UserRank(LoginRequiredMixin, TemplateView):
    template_name = "user_rank.html"

class Task(LoginRequiredMixin, TemplateView):
    template_name = "task.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = TaskModel.objects.all()
        context['tasks'] = tasks
        return context

    
