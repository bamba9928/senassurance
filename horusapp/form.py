from django import forms
from django.core.exceptions import ValidationError
from .models import Vehicule

class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = [
            'apporteur',
            'souscripteur',
            'immatriculation',
            'marque_et_modele',
            'police',
            'duree_en_mois',
            'date_effet',
            'date_echeances',
            'categorie',
            'puissance_fiscale',
            'nombre_de_place',
            'nom_du_client',
            'prenom_du_client',
            'adresse',
            'telephone',
            'mail',
            'avance',
            'reste',
            'payer',
            'note',
        ]
        widgets = {
            'apporteur': forms.Select(attrs={'class': 'form-select form-control-sm'}),
            'souscripteur': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
            'immatriculation': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
            'marque_et_modele': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'police': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '50'}),
            'duree_en_mois': forms.Select(attrs={'class': 'form-select form-control-sm'}),
            'date_effet': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'}),
            'date_echeances': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'}),
            'categorie': forms.Select(attrs={'class': 'form-select form-control-sm'}),
            'puissance_fiscale': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min': '0'}),
            'nombre_de_place': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min': '0'}),
            'nom_du_client': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'prenom_du_client': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
            'avance': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'step': '0.01'}),
            'reste': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'step': '0.01'}),
            'payer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'note': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        }

    def clean_date_echeances(self):
        date_effet = self.cleaned_data.get('date_effet')
        date_echeances = self.cleaned_data.get('date_echeances')
        if date_echeances and date_effet and date_echeances <= date_effet:
            raise ValidationError("La date d'échéance doit être postérieure à la date d'effet.")
        return date_echeances

    def clean(self):
        cleaned_data = super().clean()
        avance = cleaned_data.get('avance')
        reste = cleaned_data.get('reste')
        total = avance + reste if avance and reste else None
        if total is not None and total < 0:
            raise ValidationError("L'avance et le reste ne peuvent pas donner une somme négative.")
        return cleaned_data
