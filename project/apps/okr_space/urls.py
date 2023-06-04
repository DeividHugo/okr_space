from django.urls import path, include
from .views import Dashboard, Home

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

home = [
    path(
        'home', 
        Home.as_view(),
        name='home'
    )
]


urlpatterns = (api + dashboard + home)