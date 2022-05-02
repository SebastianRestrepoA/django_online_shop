from django import forms

class Contacto(forms.Form):

    asunto = forms.CharField()
    correo = forms.EmailField()
    mensaje = forms.CharField()
