from django.urls import path, include
from .views import Dashboard, Home, Project

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

project = [
    path(
        'project',
        Project.as_view(),
        name='project'
    )
]


urlpatterns = (api + dashboard + home + project)