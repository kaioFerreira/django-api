from rest_framework import serializers
from .models import Acompanhamento

class AcompanhamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acompanhamento
        fields = (
            'acp_id',
            'acp_prc_id',
            'acp_plt_id',
            'acp_tipo',
            'acp_esp',
            'acp_data_cumprimento',
            'acp_data_evento',
            'acp_data_prazo',
            'acp_data_cadastro',
            'acp_data'
        )