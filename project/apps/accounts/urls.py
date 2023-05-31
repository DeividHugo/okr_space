from django.urls import path, include
from apps.accounts.views import SignUpView
from django.contrib.auth.views import LogoutView

app_name = 'account'

auth = [
    path(
        'singup/', 
        SignUpView.as_view(), 
        name='singup',
    ),
    
    path(
        'logout/',
        LogoutView.as_view(
            template_name='two_factor/core/logout.html'    
        ),
        name='logout',
    ),
]

urlpatterns = auth