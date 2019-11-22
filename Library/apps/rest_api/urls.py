from django.urls import path, re_path

from Library.apps.rest_api.views import GetReaderInfoViewSet, ExportAllDataViewSet

urlpatterns = [
    path('api/v1/export_all_data/', ExportAllDataViewSet.as_view(), name="export_all_data"),
    re_path(r'api/v1/get_reader_info/(?P<id>\d*?)/$', GetReaderInfoViewSet.as_view(), name='get_user_info'),
]
