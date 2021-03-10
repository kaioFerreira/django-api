
import unittest
from django.test import TestCase
from django.urls import resolve
from django.test import Client

class TestViews(TestCase):
    def test_insert1(self):
        c = Client()

        response  = c.post('/acompanhamento100/')
        self.assertEqual(response.status_code, 200)