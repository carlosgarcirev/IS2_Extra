from django import forms

class InfoRequestForm(forms.Form):
    name = forms.CharField(max_length=100,label='Name')
    email = forms.EmailField(label='Email')
    notes = forms.CharField(widget=forms.Textarea, label='Notes')