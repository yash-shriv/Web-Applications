from django import forms
from .models import Receipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Receipe
        fields = ['receipe_name', 'receipe_description', 'receipe_image']
