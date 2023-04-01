from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_nacimieto=forms.DateField()
   
class BuscarPersonaForm(forms.Form):
    criterio_nombre=forms.CharField(max_length=100)

class BuscarTareaForm(forms.Form):
    criterio_tarea=forms.CharField(max_length=100)

class BuscarMascotaForm(forms.Form):
    criterio_mascota=forms.CharField(max_length=100)