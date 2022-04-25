"""tienda_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_productos/', views.vista_busqueda_productos),
    path('obtener_producto/', views.obtener_producto),
    path('agregar_producto/', views.agregar_producto, name='add-prods'),
    path('mostrar_productos/', views.mostrar_productos, name='show-prods'),
    path('editar_producto/<int:pk>', views.editar_producto, name='edit-prods'),
    path('eliminar_producto/<int:pk>', views.eliminar_producto, name="del-prods"),
]
