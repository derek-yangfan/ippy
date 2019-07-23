from django import forms
from js.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "country", "city"]
