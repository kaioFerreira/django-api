from django.shortcuts import render
from rest_framework import viewsets
from core.models import Acompanhamento
from core.serializers import AcompanhamentoSerializer

class Acompanhamento(viewsets.ModelViewSet):
    dados = [ {
		"acp_prc_id": 1,
		"acp_plt_id": 18,
		"acp_tipo": "KAIO",
		"acp_esp": "Sentença parcialmente procedente",
		"acp_data_cumprimento": "2020-04-23 14:50:00",
		"acp_data_evento": "2020-02-05 00:00:00",
		"acp_data_prazo": "2020-02-15 00:00:00",
		"acp_data_cadastro": "2020-02-05 13:39:00",
		"acp_data": "2020-04-11 14:51:00"
    },
    {
		"acp_prc_id": 1,
		"acp_plt_id": 18,
		"acp_tipo": "KAIO",
		"acp_esp": "Sentença parcialmente procedente",
		"acp_data_cumprimento": "2020-04-23 14:50:00",
		"acp_data_evento": "2020-02-05 00:00:00",
		"acp_data_prazo": "2020-02-15 00:00:00",
		"acp_data_cadastro": "2020-02-05 13:39:00",
		"acp_data": "2020-04-11 14:51:00"
    },
    {
		"acp_prc_id": 1,
		"acp_plt_id": 18,
		"acp_tipo": "KAIO",
		"acp_esp": "Sentença parcialmente procedente",
		"acp_data_cumprimento": "2020-04-23 14:50:00",
		"acp_data_evento": "2020-02-05 00:00:00",
		"acp_data_prazo": "2020-02-15 00:00:00",
		"acp_data_cadastro": "2020-02-05 13:39:00",
		"acp_data": "2020-04-11 14:51:00"
    },
    {
		"acp_prc_id": 1,
		"acp_plt_id": 18,
		"acp_tipo": "KAIO",
		"acp_esp": "Sentença parcialmente procedente",
		"acp_data_cumprimento": "2020-04-23 14:50:00",
		"acp_data_evento": "2020-02-05 00:00:00",
		"acp_data_prazo": "2020-02-15 00:00:00",
		"acp_data_cadastro": "2020-02-05 13:39:00",
		"acp_data": "2020-04-11 14:51:00"
    }]
    for i in range(0,3):
        print(i)
        acp = Acompanhamento(
            acp_prc_id = dados[i]['acp_prc_id'],
            acp_plt_id = dados[i]['acp_plt_id'],
            acp_tipo = dados[i]["acp_tipo"],
            acp_esp = dados[i]["acp_esp"],
            acp_data_cumprimento = dados[i]["acp_data_cumprimento"],
            acp_data_evento = dados[i]["acp_data_evento"],
            acp_data_prazo = dados[i]["acp_data_prazo"],
            acp_data_cadastro = dados[i]["acp_data_cadastro"],
            acp_data = dados[i]["acp_data"]
        )

    acp.save()
    serializer_class = AcompanhamentoSerializer