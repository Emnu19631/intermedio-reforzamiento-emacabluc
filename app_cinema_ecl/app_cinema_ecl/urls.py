from django.contrib import admin
from django.urls import path
from cine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 7. Home del cine
    path('', views.home_view, name='home'),
    
    # 1. Listado de películas
    path('peliculas/', views.peliculas_list_view, name='peliculas_list'),
    
    # 2. Detalle de película
    path('peliculas/<int:id>/', views.pelicula_detail_view, name='pelicula_detail'),
    
    # 3. Funciones de una película
    path('peliculas/<int:id>/funciones/', views.funciones_list_view, name='funciones_list'),
    
    # 4. Entradas vendidas de una función
    path('funciones/<int:id>/entradas/', views.entradas_list_view, name='entradas_list'),
    
    # 5. Snacks comprados por una entrada
    path('entradas/<int:id>/snacks/', views.snacks_list_view, name='snacks_list'),
    
    # 6. Cartelera activa
    path('cartelera/', views.cartelera_view, name='cartelera'),

    path('peliculas/', views.peliculas_list_view, name='peliculas_list'),

    path('peliculas/unica/', views.pelicula_unica_view, name='pelicula_unica'),

    path('peliculas/contiene/', views.peliculas_contiene_view, name='peliculas_contiene'),

    path('peliculas/termina/', views.peliculas_termina_view, name='peliculas_termina'),

    path('funciones/orden-mixto/', views.funciones_orden_mixto_view, name='funciones_orden_mixto'),

    path('entradas/rango/', views.entradas_rango_view, name='entradas_rango'),

    path('snacks/prefijo/', views.snacks_prefijo_view, name='snacks_prefijo'),

    path('peliculas/actualizar/', views.peliculas_actualizar_view, name='peliculas_actualizar'),

    path('entradas/<int:id>/eliminar/', views.entrada_eliminar_view, name='entrada_eliminar'),

    path('snacks/actualizar-precios/', views.snacks_actualizar_precios_view, name='snacks_actualizar_precios'),
]