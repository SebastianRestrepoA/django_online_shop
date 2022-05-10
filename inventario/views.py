from django.shortcuts import render, redirect
from django.http import HttpResponse
from inventario.models import Productos

# Create your views here.

def vista_busqueda_productos(request):

    return render (request, "search_products.html")

def obtener_producto(request):

    mensaje = "El articulo buscado: %r" %request.GET["prd"]

    return HttpResponse(mensaje)

def mostrar_productos(request):

    productos = Productos.objects.all()
    return render(request,'show_products.html',{'productos':productos})

def agregar_producto(request):

    if request.method=="POST":

        nombre = request.POST["nombre"]
        categoria = request.POST["categoria"]
        costo = request.POST["costo"]
        stock = request.POST["stock"]
        descripcion = request.POST["descripcion"]
        data = Productos(name=nombre, category=categoria, cost=costo, cantidad_stock= stock, description=descripcion)
        data.save()

        return redirect('/mostrar_productos/')
    
    else:

        return render (request, "add_products.html")

def editar_producto(request,pk):
    producto = Productos.objects.get(id=pk)
    if request.method == 'POST':

        producto.name = request.POST["nombre"]
        producto.category = request.POST["categoria"]
        producto.cost = request.POST["costo"]
        producto.cantidad_stock = request.POST["stock"]
        producto.description = request.POST["descripcion"]
        producto.save()
        return redirect('/mostrar_productos/')

    else:

        context = {
            'productos': producto,
        }

        return render(request,'edit_product.html',context)

def eliminar_producto(request, pk):

    producto = Productos.objects.get(id=pk)

    if request.method == 'POST':
        producto.delete()
        return redirect('/mostrar_productos/')
    else:

        context = {
            'producto': producto,
        }

        return render(request, 'delete_product.html', context)

