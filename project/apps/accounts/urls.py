from django.urls import path, include
from apps.accounts.views import SingUpUserView

app_name = 'account'

auth = [
    path(
        'singup/', 
        SingUpUserView.as_view(), 
        name='singup',
    )
]

urlpatterns = auth