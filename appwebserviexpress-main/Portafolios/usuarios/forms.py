from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.forms.models import fields_for_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import UsuarioWeb

class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre',required=True)
    last_name = forms.CharField(label='Apellidos',required=True)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if UsuarioWeb.objects.filter(email=email).exists():
            raise ValidationError("Ya exsite un usuario con este Email.")
        return email    

    class Meta:

        model = UsuarioWeb
        fields = ('username','first_name' ,'last_name' , 'email', 'password1', 'password2', 'fecha_nacimiento') 

    def __init__(self, *args, **kwargs):

        super(RegistrationForm, self).__init__(*args,**kwargs)


        for field in self.fields:
            
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'autocomplete': 'off'})

 
        for field in self.fields.values():
                field.help_text = None

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):

        super(LoginForm, self).__init__(*args,**kwargs)

        for field in self.fields:
            
            self.fields[field].widget.attrs.update({'class': 'input100'})
            self.fields[field].widget.attrs.update({'autocomplete': 'off'})    