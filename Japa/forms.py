from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class LoginForm(AuthenticationForm):
    pass

class NyBestillingForm(forms.ModelForm):
    class Meta:
        model = NyBestilling
        fields = ['Leveringsadresse', 'Leveringsadresse_type', 'Dørnummer', 'Leverings_tid', 'Leveringsgebyr', 'Total_pris']

class NyKategoriForm(forms.ModelForm):
    Billede = forms.ImageField()

    class Meta:
        model = NyKategori
        fields = ['Navn']

    def save(self, commit=True):
        instance = super(NyKategoriForm, self).save(commit=False)
        instance.set_image(self.cleaned_data['Billede'])
        if commit:
            instance.save()
        return instance

class NyRestaurantForm(forms.ModelForm):
    Billede = forms.ImageField()
    Kategorier = forms.ModelMultipleChoiceField(
        queryset=NyKategori.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = NyRestaurant
        fields = ['Navn', 'Adresse', 'Beskrivelse', 'Åbningstid', 'Lukketid', 'Leveringsgebyr', 'Minimumsordre', 'Kategorier']

    def save(self, commit=True):
        instance = super(NyRestaurantForm, self).save(commit=False)
        instance.set_image(self.cleaned_data['Billede'])
        if commit:
            instance.save()
            self.save_m2m()
        return instance

class NyUnderkategoriForm(forms.ModelForm):
    Kategori = forms.ModelMultipleChoiceField(
        queryset=NyKategori.objects.all(),
        widget=forms.CheckboxSelectMultiple
        )

    class Meta:
        model = NyUnderkategori
        fields = ['Navn', 'Kategori']

    def save(self, commit=True):
        instance = super(NyUnderkategoriForm, self).save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance

class NytMadForm(forms.ModelForm):
    Billede = forms.ImageField()
    Underkategori = forms.ModelMultipleChoiceField(queryset=NyUnderkategori.objects.all())

    class Meta:
        model = NytMad
        fields = ['Navn', 'Beskrivelse', 'Pris', 'Underkategori']

    def save(self, commit=True):
        instance = super(NytMadForm, self).save(commit=False)
        instance.set_image(self.cleaned_data['Billede'])
        if commit:
            instance.save()
            instance.Underkategori.set(self.cleaned_data['Underkategori'])  # Update this line
        return instance
