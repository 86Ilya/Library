import hashlib
import json

from rest_framework.test import APITestCase
from django.urls import reverse

from Library.apps.rest_api.management.commands.populate import populate_db


class LibraryTest(APITestCase):
    multi_db = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        populate_db(100, 20)

    def test_get_user_info(self):
        url = reverse('get_user_info', kwargs={'id': 10})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        m = hashlib.md5()
        m.update(b'10')
        content = json.loads(response.content)
        # according to the populate function the name is result of md5(id)
        self.assertEqual(content["name"], m.hexdigest())

    def test_export_all_data(self):
        url = reverse('export_all_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        keys, values = response.content.split(b"\r\n")[:2]
        page1_of_all_data = dict(zip(keys.split(b","), values.split(b",")))
        self.assertEqual(page1_of_all_data[b"highest_count"], b'100')
