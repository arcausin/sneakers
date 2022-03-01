from django import forms
from .models import Produit

# creating a form
class ProduitForm(forms.ModelForm):

    # create meta class
    class Meta:
        #specify model to be used
        model = Produit

        # specify fields to be used
        fields = [
            "name",
            "image",
            "description",
            "quantity",
        ]