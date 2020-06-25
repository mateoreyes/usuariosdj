from django import forms

from .models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    # se le agrega un campo contraseña, no relacionado al modelo
    # ya que la contraseña no debe ser guardada en texto plano

    password1 =  forms.CharField(
        label='Contraseña',
        required=True,
    )

    password2 =  forms.CharField(
        label='Repetir',
        required=True,
    )

    class Meta:
        """Meta definition for UserRegisterform."""
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    # validar las contraseñas, por defecto es clean_nombreAtributo a validar
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contraseñas no coinciden')
