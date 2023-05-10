from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class ChangeNameForm(forms.Form):
    name = forms.CharField(
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Имя',
                'required': True,
            }
        )
    )

class SendMessage(forms.Form):
    message = forms.CharField(
        label = '',
        widget = forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder': 'Сообщение',
                'required': True,
            }
        )
    )