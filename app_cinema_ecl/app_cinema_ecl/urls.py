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
]