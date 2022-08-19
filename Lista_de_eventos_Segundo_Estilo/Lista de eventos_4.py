from Lista_de_eventos import Lista_de_eventos_obj
#
# La menor cantidad de lineas posibles
#
id_entrada=input("Digite el id  del evento a buscar: ")
for i in Lista_de_eventos_obj.list:
    if(i==id_entrada):
        print("Encontrado")
    else:
        print("No encontrado")