from django import forms

class VacanteDetailForm(forms.Form):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":20, "class" : "form-control my-auto"}))