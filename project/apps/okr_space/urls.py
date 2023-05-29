from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.okr_space.api.api_urls')),
]