from django.views.generic import TemplateView
from two_factor.views.mixins import OTPRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"