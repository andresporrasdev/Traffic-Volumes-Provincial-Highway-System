from django import forms
from .models import TrafficData

class TrafficDataForm(forms.ModelForm):
    class Meta:
        model = TrafficData
        fields = ['id', 'sectionID', 'highway', 'section', 'sectionLength', 'sectionDescription', 'date', 'description', 'group', 'type', 'county', 'adt', 'direction']