from django import forms
from .models import Exp

class expenseForm(forms.ModelForm):
    class Meta:
        model = Exp
        fields = '__all__'
