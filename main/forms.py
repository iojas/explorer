from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-fieldset ui-input __first'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-fieldset ui-input __second'}))
    message = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-fieldset ui-input __third'})
    )
