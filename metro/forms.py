from django import forms

from .models import Station

class TrajetForm(forms.Form):
    depart = forms.ChoiceField(choices = [])
    arrive = forms.ChoiceField(choices = [])
    def __init__(self, *args, **kwargs):
        super(TrajetForm, self).__init__(*args, **kwargs)
        self.fields['depart'].choices = [(x.pk, x.nom) for x in Station.objects.all()]
        self.fields['arrive'].choices = [(x.pk, x.nom) for x in Station.objects.all()]