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
            'logradouro',
            'bairro',
            'municipio',
            'uf',
            'telefone',
            'foto',
        ]
        labels = {
            'titulo': 'Título*',
            'descricao': 'Descrição*',
            'tipo': 'Tipo imóvel*',
            'qt_quartos': 'Quartos*',
            'area': 'Área (m²)',
            'qt_vagas_garagem': 'Vagas na garagem*',
            'vl_aluguel': 'Aluguel (R$)*',
            'cep': 'CEP*',
            'logradouro': 'Logradouro',
            'bairro': 'Bairro',
            'municipio': 'Município',
            'uf': 'UF',
            'telefone': 'Telefone*',
            'foto': 'Imagem',
        }
        widgets = {
            'descricao': widgets.Textarea(attrs={'class': 'materialize-textarea'}),
        }