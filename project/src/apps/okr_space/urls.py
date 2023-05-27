from django.urls import path, include

urlpatterns = [
    path('api/', include('src.apps.okr_space.api.api_urls')),
]