from django import forms
from cheap_pints.models import Bar, Beer, PintPrice


class BarForm(forms.ModelForm):
    """The form for handling new bar input"""
     
    barName = forms.CharField(help_text="Please enter the Bar Name.",
                             widget=forms.TextInput(attrs={'placeholder': 'Search and Select Bar'}),
                            max_length=Bar.NAME_MAX_LENGTH,
                           label="Bar Name:",
                           required=True)


    googleId = forms.CharField(max_length=Bar.NAME_MAX_LENGTH, 
                                required=True,
                                widget=forms.HiddenInput)

    class Meta:
        model = Bar
        fields = ('barName','googleId')


class BeerForm(forms.ModelForm):
    BeerName = forms.CharField(help_text="Enter the Beer Name",
                        widget=forms.TextInput(attrs={'placeholder': 'Enter the Beer Name'}),
                        max_length=Bar.NAME_MAX_LENGTH,
                        label="Beer Name:",
                        required=True)

    BeerBrand = forms.CharField(help_text="(Optional)",
                            widget=forms.TextInput(attrs={'placeholder': 'Enter the Beer Brand (Optional)'}),
                            max_length=Bar.NAME_MAX_LENGTH,
                            label="Bar Brand:",
                           required=False)

    class Meta:
        model = Beer
        fields = ('BeerName','BeerBrand')


class PintPriceForm(forms.ModelForm):
    """The form for handling new bar input"""

    price = forms.FloatField(label="Pint Price:",
                                required=True)
    price_unit = forms.ChoiceField(initial=Bar.POUND,
                                                required=True,
                                                choices=Bar.PRICE_UNITS)
    class Meta:
        model = PintPrice
        fields = ('price', 'price_unit')