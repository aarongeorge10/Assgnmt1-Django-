from django import forms
from .models import crud

class AddForm(forms.ModelForm):
    class Meta:
        model = crud

        fields = ('name','age','username','password')

        widgets ={
            
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),

        }
