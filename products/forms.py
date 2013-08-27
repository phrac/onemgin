from django import forms

class ProductForm(forms.Form):
    code = forms.CharField()
