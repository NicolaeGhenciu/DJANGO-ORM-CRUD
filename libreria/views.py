from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from .models import Comentario
from django.utils import timezone

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def is_authenticated(request):
    return request.user.is_authenticated

@login_required(login_url='/login/')
def inicio(request):
    return render(request, 'paginas/inicio.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('libros')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login/')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

@login_required(login_url='/login/')
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

@login_required(login_url='/login/')
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

@login_required(login_url='/login/')
def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None,
                           request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

@login_required(login_url='/login/')
def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

@login_required(login_url='/login/')
def like(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    libro.likes += 1
    libro.save()
    return redirect('libros')

@login_required(login_url='/login/')
def comentar(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    comentarios = Comentario.objects.filter(libro=libro)
    if request.method == 'POST':
        comentario = request.POST['comentario']
        autor = request.POST['autor']
        fecha = timezone.now()
        c = Comentario(libro=libro, comentario=comentario,
                       autor=autor, fecha=fecha)
        c.save()
        return redirect('libros')
    return render(request, 'libros/comentar.html', {'libro': libro, 'comentarios': comentarios})
    
@login_required(login_url='/login/')
def ver_comentarios(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    comentarios = Comentario.objects.filter(libro=libro)
    return render(request, 'libros/comentarios.html', {'libro': libro, 'comentarios': comentarios})
