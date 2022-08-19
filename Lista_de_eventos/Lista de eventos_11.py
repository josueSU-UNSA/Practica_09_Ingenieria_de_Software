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
def buscar(lista_eventos_entrada_ids,id_evento_buscado):
    for i in lista_eventos_entrada_ids:
        if(id_evento_buscado==i):
            return True
    return False

# Uso de la funcion

lista_obj=Lista_de_eventos()

for i in range(5):
    lista_obj.agregar_evento(i)

if(buscar(lista_obj.lista,4)):
    print("Encontrado")
else:
    print("No encontrado")