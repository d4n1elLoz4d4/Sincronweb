from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .models import categoria, estadogestion, subcategoria, servicioOfrecido
from .forms import EstadoGestionForms, categoriaForms, subcategoriaForms, servicioOfrecidoForms

def inicio(request):
    titulo='inicio'
    context={
        'titutlo':titulo,
    }
    return render(request,'index.html',context)

#vista EstadoGestion
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
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear Estado Gestión'}) 

def editarreg(request, id):
    gestion= estadogestion.objects.get(idEstadoGestion=id)
    formulario = EstadoGestionForms(request.POST or None, instance=gestion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('estadogestion')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar Estado Gestión'})

def eliminareg(request, id):
    estado = estadogestion.objects.get(idEstadoGestion = id)
    estado.delete()
    return redirect('estadogestion')

#vista Categorias
def categoriaview(request):
    titulo='categoria'
    context={
        'titutlo':titulo,
    }
    lista = categoria.objects.all()
    print(lista)
    return render(request,'categoria/categoria.html',{'ListaCategorias':lista})


def editarCategoria(request, id):
    item= categoria.objects.get(idCategoria=id)
    formulario = categoriaForms(request.POST or None, instance=item)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('categoria')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar Categoría'})

def eliminarCategoria(request, id):
    item = categoria.objects.get(idCategoria = id)
    item.delete()
    return redirect('categoria')

def crearcategoria(request):
    formulario = categoriaForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('categoria')
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear Categoría'})    

        
#vista subcategoria
def subcategoriaview(request):
    titulo='subcategoria'
    context={
        'titutlo':titulo,
    }
    lista = subcategoria.objects.all()
    print(lista)
    return render(request,'subcategoria/subcategoria.html',{'ListasubCategorias':lista})


def editarsubCategoria(request, id):
    item= subcategoria.objects.get(idSubcategoria=id)
    formulario = subcategoriaForms(request.POST or None, instance=item)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('subcategoria')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar subCategoría'})

def eliminarsubCategoria(request, id):
    item = subcategoria.objects.get(idSubcategoria = id)
    item.delete()
    return redirect('subcategoria')

def crearsubcategoria(request):
    formulario = subcategoriaForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('subcategoria')
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear SubCategoría'})


#vista servicioOfrecido

def servicioOfrecidoview(request):
    titulo='servicioOfrecido'
    context={
        'titutlo':titulo,
    }
    lista = servicioOfrecido.objects.all()
    print(lista)
    return render(request,'servicioOfrecido/servicioOfrecido.html',{'ListaservicioOfrecido':lista})


def editarservicioOfrecido(request, id):
    item= servicioOfrecido.objects.get(idServicioOfrecido=id)
    formulario = servicioOfrecidoForms(request.POST or None, instance=item)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('servicioOfrecido')
    return render(request,'generico/editar.html',{'formulario':formulario, 'titulo':'Editar servicioOfrecido'})

def eliminarservicioOfrecido(request, id):
    item = servicioOfrecido.objects.get(idServicioOfrecido = id)
    item.delete()
    return redirect('servicioOfrecido')

def crearservicioOfrecido(request):
    formulario = servicioOfrecidoForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('servicioOfrecido')
    return render(request,'generico/nuevo.html',{'formulario':formulario,'titulo':'Crear servicioOfrecido'})
