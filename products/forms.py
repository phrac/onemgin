from django import forms

class ProductForm(forms.Form):
    ASIN = forms.CharField()
