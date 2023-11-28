from django import forms


class DeporteForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    juego = forms.CharField()


class EquipoForm(forms.Form):
    nombre = forms.CharField()
    pais = forms.CharField()
    ciudad = forms.CharField()


class JugadorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    posicion = forms.CharField()


class Busqueda(forms.Form):
    nombre = forms.CharField()
