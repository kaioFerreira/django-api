from django.shortcuts import render
from rest_framework import viewsets
from core.models import Acompanhamento
from core.serializers import AcompanhamentoSerializer

class AcompanhamentoViewSet(viewsets.ModelViewSet):
	queryset = Acompanhamento.objects.all()
	serializer_class = AcompanhamentoSerializer