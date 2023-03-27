from django import forms
from .models import paciente, historiaClinica, evolucion, derivacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class pacienteForm(forms.ModelForm):
    estado_choices = (
        ('activo', 'activo'),
        ('inactivo', 'inactivo'),
        ('alta', 'alta'),
        ('derivado', 'derivado')
    )
    estado = forms.ChoiceField(
        choices=estado_choices, widget=forms.RadioSelect())
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = paciente
        fields = '__all__'


class evolucionForm(forms.ModelForm):

    class Meta:
        model = evolucion
        fields = '__all__'


class derivacionForm(forms.ModelForm):

    class Meta:
        model = derivacion
        fields = '__all__'


class historiaClinicaForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = historiaClinica
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
