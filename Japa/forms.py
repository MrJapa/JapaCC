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


# class NewRestaurantForm(forms.ModelForm):
#     image = forms.ImageField()
#     categories = forms.ModelMultipleChoiceField(
#         queryset=NewCategory.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )

#     class Meta:
#         model = NewRestaurant
#         fields = ['name', 'address', 'description', 'opening_time', 'closing_time', 'delivery_fee', 'minimum_order', 'categories']

#     def save(self, commit=True):
#         instance = super(NewRestaurantForm, self).save(commit=False)
#         instance.set_image(self.cleaned_data['image'])
#         if commit:
#             instance.save()
#             self.save_m2m()  # This will save the categories
#         return instance
    
# class NewCategoryForm(forms.ModelForm):
#     image = forms.ImageField()

#     class Meta:
#         model = NewCategory
#         fields = ['name']

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.set_image(self.cleaned_data['image'])
#         if commit:
#             instance.save()
#         return instance
    
# class NewFoodForm(forms.ModelForm):
#     image = forms.ImageField()
#     undercategory = forms.MultipleChoiceField(choices=[])

#     class Meta:
#         model = NewFood
#         fields = ['name' , 'description' , 'price' , 'undercategory']

#     def __init__(self, *args, **kwargs):
#         super(NewFoodForm, self).__init__(*args, **kwargs)
#         self.fields['undercategory'].choices = [(uc.id, uc.name) for uc in NewUnderCategory.objects.all()]

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.set_image(self.cleaned_data['image'])
#         if commit:
#             instance.save()
#             self.save_m2m()
#         return instance
    
# class NewUnderCategoryForm(forms.ModelForm):
#     category = forms.MultipleChoiceField(choices=[])

#     class Meta:
#         model = NewUnderCategory
#         fields = ['name', 'category']

#     def __init__(self, *args, **kwargs):
#         super(NewUnderCategoryForm, self).__init__(*args, **kwargs)
#         self.fields['category'].choices = [(c.id, c.name) for c in NewCategory.objects.all()]

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         if commit:
#             instance.save()
#         return instance