# path: hackernews/tests.py
from django.test import TestCase
#from hackernews.views import make_absolute_location
from django.urls import reverse

class ProxyTests(TestCase):
    def test_proxy_home(self):
        # Test the proxy_home view
        response = self.client.get(reverse('proxy_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hacker News')

    def test_proxy_item(self):
        # Test the proxy_item view with a valid item ID
        item_id = 13713480
        url = reverse('proxy_item') + f'?id={item_id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'{item_id}')

    # def test_proxy_item_invalid_id(self):
    #     # Test the proxy_item view with an invalid item ID
    #     invalid_id = -1
    #     url = reverse('proxy_item') + f'?id={invalid_id}'
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 404)

# class TestAbsoluteLocation(TestCase):
#     def test_already_absolute(self):
#         absurl = make_absolute_location(
#             'https://example.com/test/path',
#             'https://example2.com/next/test/path?with=qs')
#         self.assertEquals(absurl, 'https://example2.com/next/test/path?with=qs')
#
#     def test_scheme_relative(self):
#         absurl = make_absolute_location(
#             'https://example.com/test/path',
#             '//example2.com/next/test/path?with=qs')
#         self.assertEquals(absurl, 'https://example2.com/next/test/path?with=qs')
#
#     def test_host_relative(self):
#         absurl = make_absolute_location(
#             'https://example.com/test/path',
#             '/next/test/path?with=qs')
#         self.assertEquals(absurl, 'https://example.com/next/test/path?with=qs')
#
#     def test_path_relative(self):
#         absurl = make_absolute_location(
#             'https://example.com/test/path',
#             'next/test/path?with=qs')
#         self.assertEquals(absurl, 'https://example.com/test/next/test/path?with=qs')
