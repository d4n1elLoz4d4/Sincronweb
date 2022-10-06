from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .models import estadogestion
from .forms import EstadoGestionForms

def inicio(request):
    titulo='inicio'
    context={
        'titutlo':titulo,
    }
    return render(request,'index.html',context)

def estadogestionview(request):
    titulo='gestion'
    context={
        'titutlo':titulo,
    }
    lista = estadogestion.objects.all()
    print(lista)
    return render(request,'gestion/estado_gestion.html',{'estados':lista})  

def creareg(request):
    formulario = EstadoGestionForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('estadogestion')
    return render(request,'gestion/nuevo.html',{'formulario':formulario}) 

def editarreg(request, id):
    gestion= estadogestion.objects.get(idEstadoGestion=id)
    formulario = EstadoGestionForms(request.POST or None, instance=gestion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('estadogestion')
    return render(request,'gestion/editar.html',{'formulario':formulario})

def eliminareg(request, id):
    estado = estadogestion.objects.get(idEstadoGestion = id)
    estado.delete()
    return redirect('estadogestion')

        
