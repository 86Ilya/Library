from rest_framework_csv import renderers as r
from rest_framework import generics

from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination

from Library.apps.rest_api.serializers import ReaderSerializer, BookSerializer
from Library.apps.rest_api.models import Reader, Book
from Library.settings import REST_FRAMEWORK


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = REST_FRAMEWORK["PAGE_SIZE"]


class ExportAllDataViewSet(ObjectMultipleModelAPIView):
    """
    API endpoint that allows export all data as CSV.
    Pagination is necessary, without this the database will suffer.
    """

    pagination_class = LimitPagination
    renderer_classes = (r.CSVRenderer,)
    querylist = [
        {'queryset': Reader.objects.all(), 'serializer_class': ReaderSerializer},
        {'queryset': Book.objects.all(), 'serializer_class': BookSerializer},
    ]


class GetReaderInfoViewSet(generics.RetrieveAPIView):

    """
    API endpoint that allows to fetch info about reader and all books assigned to him
    by id
    """
    lookup_field = 'id'
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
