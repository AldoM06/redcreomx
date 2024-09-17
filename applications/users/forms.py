from django import forms
from django.contrib.auth import authenticate
#
from .models import User
class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'use-keyboard-input input-group-field',
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class': 'use-keyboard-input input-group-field',
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'email',
            'username',
            'Name',
            'LastName',
            'MiddleName',
            'Curp',

        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',
                    'class': 'use-keyboard-input input-group-field',
                }
            ),
            'Username': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres ...',
                    'class': 'use-keyboard-input input-group-field',
                }
            ),
            'Name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres ...',
                    'class': 'use-keyboard-input input-group-field',
                }
            ),
            'LastName': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido ...',
                    'class': 'use-keyboard-input input-group-field',
                }
            ),
            'MiddleName': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido ...',
                    'class': 'use-keyboard-input input-group-field',
                }
            ),
            'Curp': forms.TextInput(
                attrs={
                    'placeholder': 'CURP ...',
                    'class': 'use-keyboard-input input-group-field',
                }
            ),
        }

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')

class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': ' contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return self.cleaned_data
