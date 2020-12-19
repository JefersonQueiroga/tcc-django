from django import forms
from .models import Encontros
from django.contrib.admin.widgets import AdminDateWidget

class EncontrosForms(forms.ModelForm):
    start_date = forms.DateField(widget=AdminDateWidget())
    class Meta:
        model = Encontros
        fields = ('titulo', 'descricao', 'start_date')