from .models import Services, Orders
from django import forms

class OrderForm(forms.Form):  
    additional = forms.CharField(
        label='',
        widget = forms.Textarea(
            attrs={
            'class': 'form-control',
            'placeholder': 'Также укажите технологии, которые нужно использовать, также вы можете прикрепить ссылку на задание',
            'required': True,
        })
    )