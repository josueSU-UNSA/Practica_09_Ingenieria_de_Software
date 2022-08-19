from re import S
from typing import List

#
# Clase Lista_de_eventos que nos permitira almacenar
# informacion acerca de los eventos
#
class Lista_de_eventos:
    def __init__(self):
        self.size=0
        self.lista=[]
    
    def agregar_evento(self,nuevo_id_evento):
        self.lista.append(nuevo_id_evento)
        self.size+=1
    
    def mostrar_eventos(self):
        for i in self.lista:
            print(i)


#
# Esta funcion nos permitira saber si existe un
# evento ,buscando por su ids
#
def llenado_de_lista_prueba(lista_objeto,n):
    for i in range(n):
        lista_obj.agregar_evento(i)

def buscar(lista_eventos_entrada_ids,id_evento_buscado):
    for i in lista_eventos_entrada_ids:
        if(id_evento_buscado==i):
            return True
    return False
def entrada_id():
    id_entero=input("Ingrese el id del evento: ")
    return id_entero

def mensaje(bolean_valor):
    if(bolean_valor):
        print("Encontrado")
    else:
        print("No encontrado")
# Uso de la funcion

lista_obj=Lista_de_eventos()
llenado_de_lista_prueba(lista_obj, 5)
mensaje(buscar(lista_obj.lista,entrada_id()))
lista_obj.mostrar_eventos()
