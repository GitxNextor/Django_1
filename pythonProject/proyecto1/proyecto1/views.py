from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludar(request):
    return HttpResponse("Hola Villa Urquiza!")


def segundavista(request):
    return HttpResponse("<h1>Título</h1>")


def saludo_con_nombre(request, nombre):
    return HttpResponse(f"<h1>Hola {nombre} !!!</h1>")


def calcula_anio_nacimiento(request, edad):
    anio_actual = datetime.datetime.today().year
    anio_nacimiento = anio_actual - int(edad)
    return HttpResponse(f"Naciste en el año {anio_nacimiento}")


def probandohtml(request):
    dixie = {"nombre": "Enzo", "apellido": "Gorlomi", "edad": 59}
    archivo = open(r"C:\Users\User\PycharmProjects\Other_17\pythonProject\proyecto1\plantillas\template1.html")
    contenido = archivo.read()
    archivo.close()
    template = Template(contenido)
    contexto = Context(dixie)
    documento = template.render(contexto)
    return HttpResponse(documento)
