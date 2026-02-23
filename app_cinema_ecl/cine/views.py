from django.shortcuts import render


# 7. Home del cine
def home_view(request):
    context = {
        "nombre_cine": "Cine San Marcos",
        "pelicula_destacada": "Watch Dogs: La Película",
        "total_funciones": 42
    }
    return render(request, 'cine/home.html', context)


# 1. Listado de películas
def peliculas_list_view(request):
    peliculas = [
        {"id": 1, "titulo": "Spiderman", "duracion_min": 120, "genero": "Acción", "clasificacion": "PG-13"},
        {"id": 2, "titulo": "Interstellar", "duracion_min": 169, "genero": "Ciencia Ficción", "clasificacion": "PG-13"},
    ]
    return render(request, 'cine/peliculas_list.html', {"peliculas": peliculas})


# 2. Detalle de película
def pelicula_detail_view(request, id):
    peliculas = [
        {"id": 1, "titulo": "Spiderman", "duracion_min": 120, "genero": "Acción", "clasificacion": "PG-13"},
        {"id": 2, "titulo": "Interstellar", "duracion_min": 169, "genero": "Ciencia Ficción", "clasificacion": "PG-13"},
    ]
    pelicula = next((p for p in peliculas if p["id"] == id), None)
    return render(request, 'cine/pelicula_detail.html', {"pelicula": pelicula})


# 3. Funciones de una película
def funciones_list_view(request, id):
    funciones = [
        {"hora": "15:00", "precio": 15.00, "estado": "Disponible"},
        {"hora": "18:00", "precio": 18.00, "estado": "Agotado"},
    ]
    context = {
        "pelicula": f"Película ID {id}",
        "funciones": funciones
    }
    return render(request, 'cine/funciones_list.html', context)


# 4. Entradas vendidas de una función
def entradas_list_view(request, id):
    entradas = [
        {"codigo": "E001", "asiento": "A1", "estado": "Vendido", "fecha_venta": "2026-02-01"},
        {"codigo": "E002", "asiento": "A2", "estado": "Vendido", "fecha_venta": "2026-02-01"},
    ]
    return render(request, 'cine/entradas_list.html', {"entradas": entradas})


# 5. Snacks comprados por una entrada
def snacks_list_view(request, id):
    todos_los_snacks = [
        {"entrada_id": 1, "producto": "Popcorn", "cantidad": 2, "precio_unitario": 10.50},
        {"entrada_id": 1, "producto": "Gaseosa", "cantidad": 2, "precio_unitario": 5.00},
        {"entrada_id": 2, "producto": "Nachos", "cantidad": 1, "precio_unitario": 12.00},
    ]
    snacks_filtrados = [s for s in todos_los_snacks if s["entrada_id"] == id]
    total = sum(s["cantidad"] * s["precio_unitario"] for s in snacks_filtrados)

    context = {
        "entrada_id": id,
        "snacks": snacks_filtrados,
        "total_snacks": total
    }
    return render(request, 'cine/snacks_list.html', context)


# 6. Cartelera activa
def cartelera_view(request):
    peliculas = [
        {"titulo": "Watch Dogs", "activa": True},
        {"titulo": "Matrix", "activa": False},
        {"titulo": "Inception", "activa": True},
    ]
    activas = [p for p in peliculas if p["activa"]]
    return render(request, 'cine/cartelera.html', {"peliculas": activas})