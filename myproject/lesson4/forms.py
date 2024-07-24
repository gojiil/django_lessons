from typing import Any
from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11)
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 
                                                                            'placeholder': 'Input address'}))
    
    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.team') or email.endswith('ya.ru')):
            raise forms.ValidationError('Fill out valid email!')
        return email

class ItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    image = forms.ImageField()