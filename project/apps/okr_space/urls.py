from django.urls import path, include
from .views import Dashboard

app_name = 'okr_space'

api = [
    path(
        'api/', 
        include('apps.okr_space.api.api_urls')
    ), 
]

dashboard = [
    path(
        '', 
        Dashboard.as_view(), 
        name='dashboard'
    )
]

urlpatterns = (api + dashboard)