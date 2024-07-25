from django import forms
from listings.models import Band, New

class ContactUsForm(forms.Form):
    nom = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
    
class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        exclude = ('active', 'official_homepage')

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('title', 'article', 'band')

