from django.db import models

class Acompanhamento(models.Model):
    acp_id = models.AutoField(primary_key=True)
    acp_prc_id = models.IntegerField()
    acp_plt_id = models.IntegerField()
    acp_tipo = models.CharField(max_length=1000)
    acp_esp = models.CharField(max_length=1000)
    acp_data_cumprimento = models.CharField(max_length=1000)
    acp_data_evento = models.CharField(max_length=1000)
    acp_data_prazo = models.CharField(max_length=1000)
    acp_data_cadastro = models.CharField(max_length=1000)
    acp_data = models.CharField(max_length=1000)

    class Meta:
        db_table = 'acompanhamento'

    def __str__(self):
        return self.post_title + ' - ' + self.post_body
