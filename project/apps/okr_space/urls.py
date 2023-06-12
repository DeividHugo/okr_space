from django.urls import path, include
from .views import Dashboard, Home, Project, UserRank

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

user_rank = [
    path(
        'user_rank',
        UserRank.as_view(),
        name='user_rank'
    )
]


urlpatterns = (api + dashboard + home + project + user_rank)