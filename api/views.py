from django.shortcuts import render
from rest_framework import viewsets
from core.models import Acompanhamento
from core.serializers import AcompanhamentoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class AcompanhamentoViewSet(viewsets.ModelViewSet):
	serializer_class = AcompanhamentoSerializer
	@api_view(['GET'])
	def get(request):
		queryset = Acompanhamento.objects.all()
		serializer = AcompanhamentoSerializer(queryset, many=True)
		return Response(serializer.data)

	@api_view(['POST'])
	def post(request):
		serializer = AcompanhamentoSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
		
		return Response(serializer.data)