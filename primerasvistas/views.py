


from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

from django.template import  Template,Context, loader

from primerasvistas.models import Silver


def inicio(request):
    return HttpResponse("Hola soy fernando")


def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f"Fecha actual:{fecha_actual}")
    
    
def saludo(request, nombre):
    return HttpResponse(f"Hola {nombre}")
   
#    #Version 1
# def mi_template(request):
    
#     archivo = open(
#         r"C:\Users\DavidFernandoRodrigu\Desktop\Djangoproject\templates\prueba.html", "r")
    
#     template1 = Template(archivo.read())
    
#     archivo.close()
    
#     nombre = "Fernando"
    
#     contexto1 = Context({"nombre": nombre})
    
#     render1 = template1.render(contexto1)
    
#     return HttpResponse(render1)   
   
# version 2

def mi_template(request, nombre_usuario, edad_usuario):
    
    template1 = loader.get_template("prueba.html")
    
    nombre = "Fernando"
    apellido = "Rodriguez"
    
    lista = ["David", "Fernando", "Memo", "Katia", "Esme", "Germany", 7, 8, 9,]
    
    silver = Silver(nombre= nombre_usuario, edad=edad_usuario)
    silver.save()
    
    render1 = template1.render(
        {'nombre': nombre, 'apellido': apellido, 'edad' : 5000, 'lista': lista, 'silver': silver})
    
    return HttpResponse(render1)   


def listado_usuarios(request):
    
    template = loader.get_template('listado_usuarios.html')
    
    lista_usuarios = Silver.objects.all()
    
    render = template.render({'lista_usuarios' : lista_usuarios})
    
    return HttpResponse(render)
       
   
   