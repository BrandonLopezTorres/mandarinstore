from django import forms 
from django.core import validators


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Largo! Solo personas con nombre que empiece con Z')

class FormComment(forms.Form):
    full_name = forms.CharField(validators=[validators.MaxLengthValidator(20), check_for_z])
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(150)])

class FormContact(forms.Form):
    full_name = forms.CharField(validators=[validators.MaxLengthValidator(50), check_for_z])
    address = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(150)])
    phone = forms.CharField(validators=[validators.MaxLengthValidator(20), check_for_z])
    email = forms.EmailField(validators=[validators.MaxLengthValidator(50), check_for_z])
    contact_active = forms.BooleanField()