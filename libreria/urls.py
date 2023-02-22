from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name="nosotros"),
    path('libros', views.libros, name="libros"),
    path('libros/crear', views.crear, name="crear"),
    path('libros/editar', views.editar, name="editar"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('libros/editar/<int:id>', views.editar, name="editar"),
    path('like/<int:id_libro>', views.like, name="like"),
    path('libros/<int:id_libro>/comentar', views.comentar, name="comentar"),
    path('comentarios/<int:id_libro>', views.ver_comentarios, name='ver_comentarios'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
