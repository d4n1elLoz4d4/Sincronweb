from django.shortcuts import render, redirect
from usuarios.forms import UsuarioLoginForm
from usuarios.models import UsuarioLogin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password

# Create your views here.
def usuarios(request):
    titulo="usuarios"
    usuarios= UsuarioLogin.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
        }
    return render(request,'usuarios/UsuarioLogin.html',context)
def usuarios_crear(request):
    titulo="Usuarios - Crear"
    if request.method == "POST":
        form= UsuarioLoginForm(request.POST, request.FILES)
        if form.is_valid():
            if not User.objects.filter(username=request.POST['documento']):
                user = User.objects.create_user('nombre','email@email','pass')
                user.username= request.POST['documento']
                user.first_name= request.POST['nombres']
                user.last_name= request.POST['apellidos']
                user.email= request.POST['email']
                user.password=make_password("@" + request.POST['nombres'][0] + request.POST['apellidos'][0] + request.POST['documento'][-4:])
                user.save()
                user_group = User
                my_group= Group.objects.get(name='Normal')
                usuario.user.groups.clear()
                my_group.user_set.add(usuario.user)
            else:
                user=User.objects.get(username=request.POST['documento'])

            usuario= UsuarioLogin.objects.create(
                nombres=request.POST['nombres'],
                apellidos=request.POST['apellidos'],
                foto=form.cleaned_data.get('foto'),
                email=request.POST['email'],
                tipoDocumento=request.POST['tipoDocumento'],
                documento=request.POST['documento'],
                telefono=request.POST['telefono'],
                direccion=request.POST['direccion'],  
                fecha_nacimiento=request.POST['fecha_nacimiento'],
                user=user,
            )
            return redirect('usuarios')
        else:
            form = UsuarioLoginForm(request.POST,request.FILES)
    else:
        form= UsuarioLoginForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'partials/crear.html',context)

def usuarios_editar(request, pk):
    titulo="usuarios - Editar"
    usuario= UsuarioLogin.objects.get(id=pk)
    if request.method == "POST":
        form= UsuarioLoginForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Error al guardar")
    else:
        form= UsuarioLoginForm(instance=usuario)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'partials/crear.html',context)
def usuarios_eliminar(request, pk):
    titulo="usuarios - Eliminar"
    usuarios= UsuarioLogin.objects.all()

    Usuario.objects.filter(id=pk).update(
            estado='0'
        )
    return redirect('usuarios')
        
   
    context={
        'usuarios':usuarios,
        'titulo':titulo,
     
    }
    return render(request,'usuarios/UsuarioLogin.html',context)    


    def loggedIn(request):
     if request.user.is_authenticated:
         respuesta:"Ingresado como "+ request.user.username
     else:
         respuesta:"No estas autenticado."
     return HttpResponse(respuesta)

def logout_user(request):

    return redirect('registration/login.html')
