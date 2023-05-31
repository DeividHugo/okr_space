from django.views.generic import TemplateView

class SingUpUserView(TemplateView):
    template_name = 'two_factor/core/singup.html'

