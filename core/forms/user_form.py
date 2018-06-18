from core.models.biostatistics import Biostatistic
from core.models.med_graphic import Med_graphic
from django.forms import forms

__author__ = 'andrews'


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", required=True, max_length=30)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Remember me", required=False)


class RegistrationForm(forms.Form):
    company_name = forms.CharField(
        label="Company Name", max_length=255, required=True,
        error_messages={'required': 'Company name cannot be blank'}
    )
    class Meta:
        model = Biostatistic, Med_graphic
        exclude = ('company', 'warehouses')
        widgets = {
            'street_address': forms.Textarea(attrs={'class': "md-textarea"}),
            'associated_products': forms.SelectMultiple(attrs={'class': 'mdb-select'}),
            'registered_location': forms.Select(attrs={'class': 'mdb-select'}),
            'country': forms.Select(attrs={'class': 'mdb-select'})
        }
