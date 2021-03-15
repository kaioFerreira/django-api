from django.shortcuts import render
from rest_framework import viewsets
from core.models import Acompanhamento
from core.serializers import AcompanhamentoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

class AcompanhamentoViewSet(viewsets.ModelViewSet):
	serializer_class = AcompanhamentoSerializer
	@api_view(['GET'])
	def get(request):
		queryset = Acompanhamento.objects.all()
		serializer = AcompanhamentoSerializer(queryset, many=True)
		return Response(serializer.data)

	@api_view(['POST'])
	def post(request):
		dados = [ 
			Acompanhamento(
				acp_prc_id = 1,
				acp_plt_id = 18,
				acp_tipo = "KAIO",
				acp_esp = "Sentença parcialmente procedente",
				acp_data_cumprimento = "2020-04-23 14:50:00",
				acp_data_evento = "2020-02-05 00:00:00",
				acp_data_prazo = "2020-02-15 00:00:00",
				acp_data_cadastro = "2020-02-05 13:39:00",
				acp_data = "2020-04-11 14:51:00"
			),
			Acompanhamento(
				acp_prc_id = 1,
				acp_plt_id = 18,
				acp_tipo = "KAIO",
				acp_esp = "Sentença parcialmente procedente",
				acp_data_cumprimento = "2020-04-23 14:50:00",
				acp_data_evento = "2020-02-05 00:00:00",
				acp_data_prazo = "2020-02-15 00:00:00",
				acp_data_cadastro = "2020-02-05 13:39:00",
				acp_data = "2020-04-11 14:51:00"
			)
		]
		queryset = Acompanhamento.objects.bulk_create(dados)
		
		return Response(status=status.HTTP_201_CREATED);