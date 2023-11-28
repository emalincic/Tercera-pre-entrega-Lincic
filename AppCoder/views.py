from django.shortcuts import render, redirect
from AppCoder.models import Deporte, Equipo, Jugador
from AppCoder.forms import DeporteForm, EquipoForm, JugadorForm, Busqueda


def show_html(request):
    contexto = {}
    return render(request, 'index.html', contexto)


def agregar_deporte(request):
    if request.method == "POST":
        deporteform = DeporteForm(request.POST)
        if deporteform.is_valid():
            info = deporteform.cleaned_data
            agregar_deporte = Deporte(nombre=info["nombre"], descripcion=info["descripcion"], juego=info["juego"])
            agregar_deporte.save()

            return redirect("/app/show")

    form_deporte = DeporteForm()
    contexto = {
        "form": form_deporte
    }

    return render(request, "AppCoder/agregar_deporte.html", contexto)


def mostrar_deportes(request):
    deportes = Deporte.objects.all()
    contexto = {
        "deportes": deportes,
        "form": Busqueda()
    }

    return render(request, 'AppCoder/deporte.html', contexto)

def busqueda_deporte(request):
    nombre = request.GET["nombre"]
    deportes = Deporte.objects.filter(nombre__icontains=nombre)
    contexto = {
        "deportes": deportes,
        "form": Busqueda(),
    }
    return render(request, "AppCoder/deporte.html", contexto)



def agregar_equipo(request):
    if request.method == "POST":
        equipoform = EquipoForm(request.POST)

        if equipoform.is_valid():
            info = equipoform.cleaned_data
            agregar_equipo = Equipo(nombre=info["nombre"], pais=info["pais"], ciudad=info["ciudad"])
            agregar_equipo.save()

            return redirect("/app/show")

    form_equipo = EquipoForm()

    contexto = {
        "form": form_equipo
    }

    return render(request, "AppCoder/agregar_equipo.html", contexto)


def mostrar_equipos(request):
    equipos = Equipo.objects.all()
    contexto = {
        "equipos": equipos,
        "form": Busqueda()
    }

    return render(request, 'AppCoder/equipo.html', contexto)

def busqueda_equipo(request):
    nombre = request.GET["nombre"]
    equipos = Equipo.objects.filter(nombre__icontains=nombre)
    contexto = {
        "equipos": equipos,
        "form": Busqueda(),
    }
    return render(request, "AppCoder/equipo.html", contexto)


def agregar_jugador(request):
    if request.method == "POST":
        jugadorform = JugadorForm(request.POST)
        if jugadorform.is_valid():
            info = jugadorform.cleaned_data
            agregar_jugador = Jugador(nombre=info["nombre"], apellido=info["apellido"], posicion=info["posicion"])
            agregar_jugador.save()

            return redirect("/app/show")

    form_jugador = JugadorForm()

    contexto = {
        "form": form_jugador
    }

    return render(request, 'AppCoder/agregar_jugador.html', contexto)


def mostrar_jugadores(request):
    jugadores = Jugador.objects.all()
    contexto = {
        "jugadores": jugadores,
        "form": Busqueda()
    }

    return render(request, 'AppCoder/jugador.html', contexto)

def busqueda_jugador(request):
    nombre = request.GET["nombre"]
    jugadores = Jugador.objects.filter(nombre__icontains=nombre)
    contexto = {
        "jugadores": jugadores,
        "form": Busqueda(),
    }
    return render(request, "AppCoder/jugador.html", contexto)
