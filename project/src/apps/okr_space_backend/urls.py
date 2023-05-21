from django.urls import path, include

urlpatterns = [
    path('api/', include('src.apps.okr_space_backend.api.api_urls')),
]