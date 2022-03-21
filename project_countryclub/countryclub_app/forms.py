from django import forms
from django.core.validators import RegexValidator
from django.forms import Select, DateInput
from .models import *


class ClubForm(forms.ModelForm):
    city = forms.CharField(max_length=128,
                           required=True,
                           validators=[RegexValidator("[A-Za-z]+",
                                                      message="City can only contain letters")])
    address = forms.CharField(max_length=512, required=True)

    class Meta:
        model = Club
        fields = ['city', 'address']
