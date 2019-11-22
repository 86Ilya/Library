from django.db import connections
from django.core.management.base import BaseCommand

from Library.settings import MAXBOOKS, MAXREADERS, DATABASES


def populate_db(maxbooks, maxreaders):
    """
    Function populates database with test data.
    Raw sql is much faster then Django ORM in this case.
    """

    insert_readers = f"INSERT INTO rest_api_reader(id, name) \
        SELECT  generate_series(1,{maxreaders}) AS id, md5(generate_series(1,{maxreaders})::text) AS name;"

    insert_books = f"INSERT INTO rest_api_book(id, title) \
        SELECT  generate_series(1,{maxbooks}) AS id, md5(generate_series(1,{maxbooks})::text) AS title;"

    insert_books_readers_relations = f"INSERT INTO rest_api_reader_books(id, reader_id, book_id) \
        SELECT generate_series(1,{maxbooks + maxreaders}) AS id, \
        floor(random() * {maxreaders}+ 1)::int as reader_id, \
        floor(random() * {maxbooks}+ 1)::int as book_id \
        ON CONFLICT \
        DO NOTHING;"

    for db in list(DATABASES):
        with connections[db].cursor() as cursor:
            cursor.execute(insert_books)
            cursor.execute(insert_readers)
            cursor.execute(insert_books_readers_relations)


class Command(BaseCommand):
    help = 'Populate database with test data'

    def handle(self, *args, **options):
        populate_db(MAXBOOKS, MAXREADERS)
