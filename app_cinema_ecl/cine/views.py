from django.shortcuts import render, redirect
from django.db.models import F
from pelicula.models import Pelicula
from funcion.models import Funcion
from entrada.models import Entrada, SnackCompra


# ==========================================
# VISTAS ANTERIORES (Reforzamiento 1 y 2)
# ==========================================

def home_view(request):
    cantidad_funciones = Funcion.objects.count()

    context = {
        "nombre_cine": "Cine San Marcos",
        "pelicula_destacada": "Watch Dogs: La Película",
        "total_funciones": cantidad_funciones
    }
    return render(request, 'cine/home.html', context)


def cartelera_view(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'cine/cartelera.html', {"peliculas": peliculas})


def pelicula_detail_view(request, id):
    try:
        pelicula = Pelicula.objects.get(id=id)
    except Pelicula.DoesNotExist:
        pelicula = None
    return render(request, 'cine/pelicula_detail.html', {"pelicula": pelicula})


def funciones_list_view(request, id):
    funciones = Funcion.objects.filter(pelicula_id=id)
    context = {
        "pelicula": f"Película ID {id}",
        "funciones": funciones
    }
    return render(request, 'cine/funciones_list.html', context)


def entradas_list_view(request, id):
    entradas = Entrada.objects.filter(funcion_id=id)
    return render(request, 'cine/entradas_list.html', {"entradas": entradas})


def snacks_list_view(request, id):
    snacks_filtrados = SnackCompra.objects.filter(entrada_id=id)
    total = sum(s.cantidad * s.precio_unitario for s in snacks_filtrados)
    context = {
        "entrada_id": id,
        "snacks": snacks_filtrados,
        "total_snacks": total
    }
    return render(request, 'cine/snacks_list.html', context)


# ==========================================
# NUEVAS VISTAS (Reforzamiento 03)
# ==========================================

# 1) Listado completo de películas
def peliculas_list_view(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'cine/peliculas_list.html', {"peliculas": peliculas})


# 2) Obtener UNA película por datos exactos
def pelicula_unica_view(request):
    titulo = request.GET.get('titulo', '')
    clasificacion = request.GET.get('clasificacion', '')
    try:
        pelicula = Pelicula.objects.get(titulo=titulo, clasificacion=clasificacion)
    except Pelicula.DoesNotExist:
        pelicula = None
    return render(request, 'cine/pelicula_unica.html', {"pelicula": pelicula})


# 3) Búsqueda por parte del título (contains)
def peliculas_contiene_view(request):
    texto = request.GET.get('texto', '')
    peliculas = Pelicula.objects.filter(titulo__icontains=texto) if texto else []
    return render(request, 'cine/peliculas_contiene.html', {"peliculas": peliculas, "texto": texto})


# 4) Filtro por últimos caracteres (endswith)
def peliculas_termina_view(request):
    texto = request.GET.get('texto', '')
    peliculas = Pelicula.objects.filter(titulo__endswith=texto) if texto else []
    return render(request, 'cine/peliculas_termina.html', {"peliculas": peliculas, "texto": texto})


# 5) Ordenamiento mixto en funciones
def funciones_orden_mixto_view(request):
    funciones = Funcion.objects.all().order_by('estado', '-fecha_hora')
    return render(request, 'cine/funciones_orden_mixto.html', {"funciones": funciones})


# 6) Slicing: mostrar rango de entradas
def entradas_rango_view(request):
    entradas = Entrada.objects.all()[4:7]
    return render(request, 'cine/entradas_rango.html', {"entradas": entradas})


# 7) Filtrar por prefijo para snacks
def snacks_prefijo_view(request):
    texto = request.GET.get('texto', '')
    snacks = SnackCompra.objects.filter(producto__startswith=texto) if texto else []
    return render(request, 'cine/snacks_prefijo.html', {"snacks": snacks, "texto": texto})


# 8) Actualización masiva con update()
def peliculas_actualizar_view(request):
    nueva_clasificacion = request.GET.get('nueva_clasificacion')
    pref = "Acc"
    if nueva_clasificacion:
        Pelicula.objects.filter(genero__startswith=pref).update(clasificacion=nueva_clasificacion)

    peliculas = Pelicula.objects.filter(genero__startswith=pref).order_by("titulo")
    return render(request, 'cine/peliculas_actualizar.html', {"peliculas": peliculas})


# 9) Eliminar una entrada por ID
def entrada_eliminar_view(request, id):
    try:
        entrada = Entrada.objects.get(id=id)
        codigo_asiento = entrada.asiento
        entrada.delete()
        mensaje = f"Entrada eliminada: {codigo_asiento}"
    except Entrada.DoesNotExist:
        mensaje = "No existe esa entrada"

    return render(request, 'cine/entrada_eliminar.html', {"mensaje": mensaje})


# 10) Actualización dinámica de precios de snacks con F expressions
def snacks_actualizar_precios_view(request):
    min_precio = 10
    descuento = 2
    SnackCompra.objects.filter(precio_unitario__gte=min_precio).update(precio_unitario=F('precio_unitario') - descuento)

    snacks = SnackCompra.objects.all()
    return render(request, 'cine/snacks_actualizar_precios.html', {"snacks": snacks})