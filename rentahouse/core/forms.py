from django.forms import ModelForm, widgets
from .models import Imovel


class ImovelForm(ModelForm):
    class Meta:
        model = Imovel
        fields = [
            'titulo',
            'descricao',
            'tipo',
            'qt_quartos',
            'area',
            'qt_vagas_garagem',
            'vl_aluguel',
            'cep',
            'endereco',
            'telefone',
        ]
        labels = {
            'titulo': 'Título*',
            'descricao': 'Descrição*',
            'tipo': 'Tipo imóvel*',
            'qt_quartos': 'Quartos*',
            'area': 'Área (m²)',
            'qt_vagas_garagem': 'Vagas na garagem',
            'vl_aluguel': 'Aluguel (R$)*',
            'cep': 'CEP*',
            'endereco': 'Endereço (não será exibido no anúncio)',
            'telefone': 'Telefone*',
        }
        widgets = {
            'descricao': widgets.Textarea(attrs={'class': 'materialize-textarea'})
        }