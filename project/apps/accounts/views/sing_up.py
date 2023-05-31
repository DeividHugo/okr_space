from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from apps.accounts.forms import SignUpForm

class SignUpView(CreateView):
    template_name = 'two_factor/core/singup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('two_factor:login')
    model = User