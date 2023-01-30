from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from .models import Comentario
from django.utils import timezone

# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})


def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})


def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None,
                           request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})


def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')


def like(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    libro.likes += 1
    libro.save()
    return redirect('libros')


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

def ver_comentarios(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    comentarios = Comentario.objects.filter(libro=libro)
    return render(request, 'libros/comentarios.html', {'libro': libro, 'comentarios': comentarios})
