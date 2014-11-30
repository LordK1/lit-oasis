from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(required=True, max_length=40)
    email = forms.EmailField(required=False, max_length=100)
    first_name = forms.CharField(required=False, max_length=50)
    last_name = forms.CharField(required=False, max_length=50)
    message = forms.CharField(required=True, widget=forms.Textarea)
