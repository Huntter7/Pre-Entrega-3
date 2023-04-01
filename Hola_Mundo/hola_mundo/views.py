from django.shortcuts import render
from hola_mundo.models import Persona, Tareas, Mascotas
from hola_mundo.forms import PersonaForm, BuscarPersonaForm, BuscarTareaForm, BuscarMascotaForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

def mostrar_personas(request):

    personas=Persona.objects.all()
    total_personas=len(personas)
    context = {
        'personas' : personas,
        'total_personas' : total_personas,
        'form': PersonaForm()
    }
    return render(request, 'hola_mundo/personas.html', context)

def crear_personas(request):
    f=PersonaForm(request.POST)
    context = {
        'form':f
    }
   
    if f.is_valid():
        Persona(nombre = f.data['nombre'], 
                apellido = f.data['apellido'], 
                fecha_nacimieto = f.data['fecha_nacimieto']).save()
        context['form'] = PersonaForm()

    f=PersonaForm(request.POST)
    personas=Persona.objects.all()
    total_personas=len(personas)

    context['personas'] = personas
    context['total_personas'] = total_personas

    return render(request, 'hola_mundo/personas.html', context)

class BuscarPersonas(ListView):
    model = Persona
    context_object_name = 'personas'

    def get_queryset(self):
        f = BuscarPersonaForm(self.request.GET)
        if f.is_valid():
            return Persona.objects.filter(nombre__icontains=f.data['criterio_nombre']).all()
        return Persona.objects.none()
            

def mostrar_tarea(request):
    tareas = Tareas.objects.all()
    context = {
        'tareas' : tareas
    }
    return render(request, 'hola_mundo/tareas.html', context)

class CrearTarea(CreateView):
    model = Tareas
    success_url = reverse_lazy('tareas-create')
    fields = ['nombre']

class BuscarTareas(ListView):
    model = Tareas
    context_object_name = 'tareas'

    def get_queryset(self):
        f = BuscarTareaForm(self.request.GET)
        if f.is_valid():
            return  Tareas.objects.filter(nombre__icontains=f.data['criterio_tarea']).all()
        return Tareas.objects.none()
    
def mostrar_mascotas(request):
    mascotas = Mascotas.objects.all()
    return render(request, 'hola_mundo/mascotas.html', {'mascotas':mascotas})
    
class CrearMascota(CreateView):
    model = Mascotas
    success_url = reverse_lazy('mascotas-create')
    fields = ['nombre', 'raza']

class BuscarMascota(ListView):
    model = Mascotas
    context_object_name = 'mascotas'

    def get_queryset(self):
        f = BuscarMascotaForm(self.request.GET)
        if f.is_valid():
            return  Mascotas.objects.filter(nombre__icontains=f.data['criterio_mascota']).all()
        return Mascotas.objects.none()
