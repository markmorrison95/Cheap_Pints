from django import forms
from cheap_pints.models import PintPrice


class PintPriceForm(forms.ModelForm):
    """The form for handling new bar input"""
     
    barName = forms.CharField(help_text="Please enter the Bar Name.",
                            max_length=PintPrice.NAME_MAX_LENGTH,
                           label="Bar Name:",
                           required=True)

    price = forms.FloatField(label="Pint Price:",
                                required=True)
    price_unit = forms.CharField(initial=PintPrice.PRICE_DEFAULT_UNIT,
                                    required=True)


    googleId = forms.CharField(max_length=PintPrice.NAME_MAX_LENGTH, 
                                    required=True,
                                    widget=forms.HiddenInput)

    image_reference = forms.CharField(max_length=PintPrice.URL_MAX_LENGTH,
                                    widget=forms.HiddenInput)

    class Meta:
        model = PintPrice
        fields = ('barName','price', 'price_unit')