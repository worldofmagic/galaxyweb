from django import forms

class SearchForm(forms.Form):
    target = forms.CharField(required=True, label='target')
