from django.urls import path

from AppCoder.views import show_html, agregar_deporte, agregar_equipo, agregar_jugador, mostrar_deportes, mostrar_equipos, mostrar_jugadores, busqueda_deporte, busqueda_equipo, busqueda_jugador

urlpatterns = [
    path('show/', show_html),
    path('agregar_deporte/', agregar_deporte),
    path('agregar_equipo/', agregar_equipo),
    path('agregar_jugador/', agregar_jugador),
    path('deportes/', mostrar_deportes),
    path('equipos/', mostrar_equipos),
    path('jugadores/', mostrar_jugadores),
    path('buscar_dep/', busqueda_deporte),
    path('buscar_eq/', busqueda_equipo),
    path('buscar_jug/', busqueda_jugador),
]
