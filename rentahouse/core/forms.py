from django.forms import ModelForm
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
            'vl_condominio',
            'vl_aluguel',
            'cep',
            'endereco',
            'telefone',
            'email',
        ]
        labels = {
            'titulo': 'Título*',
            'descricao': 'Descrição*',
            'tipo': 'Tipo imóvel*',
            'qt_quartos': 'Quartos*',
            'area': 'Área (m²)',
            'qt_vagas_garagem': 'Vagas na garagem',
            'vl_condominio': 'Condomínio (R$)',
            'vl_aluguel': 'Aluguel (R$)',
            'cep': 'CEP*',
            'endereco': 'Endereço',
            'telefone': 'Telefone*',
            'email': 'E-mail',
        }
