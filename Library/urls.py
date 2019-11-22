from django.urls import include, path

urlpatterns = [
    path('', include('Library.apps.rest_api.urls')),
]
