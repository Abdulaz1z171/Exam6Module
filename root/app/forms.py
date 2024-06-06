from django import forms
from app.models import Customer

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()