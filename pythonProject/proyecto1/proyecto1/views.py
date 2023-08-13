from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader


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


# Método de carga de Templates por archivo
def probandohtml(request):
    dixie = {"nombre": "Enzo", "apellido": "Gorlomi", "edad": 59,
             "lista_de_notas": [1, 9, 5, 4, 7, 8, 2]}
    archivo = open(r"C:\Users\User\PycharmProjects\Other_17\pythonProject"
                   r"\proyecto1\plantillas\template1.html")
    contenido = archivo.read()
    archivo.close()
    template = Template(contenido)
    contexto = Context(dixie)
    documento = template.render(contexto)
    return HttpResponse(documento)

# Método de carga de templates por Loader
# Es más breve, mejor organizado quizás y depende de haber importado la clase
# Loader, en la línea 3 y de haber cargado el directorio de templates en el
# archivo settings.py
# Cargó el path de las plantillas en modo absoluto en lugar de hacerlo relativo
# No aclara por qué pero esto puede joder al bajar el paquete/módulo de github
# porque no sabemos a qué directorio va a ir a parar.
# Espero que explique cómo hacerlo relativo cuanto antes.

# Acá termina el primer proyecto de Python con Django, git, github y adiós!

def probando2(request):
    dixie = {"nombre": "Enzo", "apellido": "Gorlomi", "edad": 59,
             "lista_de_notas": [10, 10, 9, 2, 3, 8, 2]}
    template = loader.get_template("template1.html")
    documento = template.render(dixie)
    return HttpResponse(documento)