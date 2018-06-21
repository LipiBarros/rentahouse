from django.forms import ModelForm, widgets
from .cleaners import manter_digitos
from .models import Imovel


class ImovelFormClean(ModelForm):
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        return manter_digitos(telefone)

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        return manter_digitos(cep)

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data


class ImovelForm(ImovelFormClean):
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