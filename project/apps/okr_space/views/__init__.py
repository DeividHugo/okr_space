from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"


class Home(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class Project(LoginRequiredMixin, TemplateView):
    template_name = "project.html"
