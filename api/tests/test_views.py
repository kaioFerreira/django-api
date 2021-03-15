
import unittest
from django.test import TestCase
from django.urls import resolve
from django.test import Client

class TestViews(TestCase):
    def test_insert1(self):
        c = Client()

        response  = c.post('/acompanhamentopost/', {
            "acp_prc_id": 1,
            "acp_plt_id": 18,
            "acp_tipo": "KAIO",
            "acp_esp": "Sentença parcialmente procedente",
            "acp_data_cumprimento": "2020-04-23 14:50:00",
            "acp_data_evento": "2020-02-05 00:00:00",
            "acp_data_prazo": "2020-02-15 00:00:00",
            "acp_data_cadastro": "2020-02-05 13:39:00",
            "acp_data": "2020-04-11 14:51:00"
        })
        self.assertEqual(response.status_code, 200)