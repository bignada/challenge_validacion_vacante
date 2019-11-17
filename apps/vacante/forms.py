from django import forms

class VacanteDetailForm(forms.Form):
    descripcion = forms.TextInput()