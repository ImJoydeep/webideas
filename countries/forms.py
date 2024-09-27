from django import forms
from .models import Country, City

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_name', 'country_code', 'country_flag']

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city_name', 'country']

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.all()
