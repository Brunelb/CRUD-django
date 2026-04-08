from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    # name = forms.CharField(label='', required=True, widget=forms.TextInput(
    #     attrs={
    #         'placeholder':'Entrez le nom du produit',
    #     }
    # ))
    # description = forms.CharField(label='', required=True, widget=forms.Textarea(
    #     attrs={
    #         'rows':8,
    #         'placeholder':'Entrez la description du produit',
    #     }
    # ))
    # price = forms.DecimalField(label='', required=True,widget=forms.NumberInput(
    #      attrs={
    #         'placeholder':'Entrez le prix du produit',
    #     }
    # ))
    # actif = forms.BooleanField(label='Actif')
    # slug =forms.CharField(label='', required=True, widget=forms.TextInput(
    #     attrs={
    #         'placeholder':'Entrez le slug du produit',
    #     }
    # ))
    class Meta:
        model = Products
        fields = ('name','description','price','actif','slug')

    # def clean_name(self, *args, **kwargs):
    #     name = self.cleaned_data.get('name')
    #     if not 'man' in name:
    #         raise forms.ValidationError('nom doit contenir man')
    #     elif not 'uba' in name:
    #         raise forms.ValidationError('nom doit contenir uba')
    #     else:
    #         return name
        
    # def clean_email(self,*args,**kwargs):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith("com"):
    #         raise forms.ValidationError('email doit se terminer avec .com')

    

class RowProductForm(forms.Form):
    name = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez le nom du produit',
        }
    ))
    description = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={
            'rows':8,
            'placeholder':'Entrez la description du produit',
        }
    ))
    price = forms.DecimalField(label='', required=True,widget=forms.NumberInput(
         attrs={
            'placeholder':'Entrez le prix du produit',
        }
    ))
    actif = forms.BooleanField(label='Actif')
    slug =forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez le slug du produit',
        }
    ))

