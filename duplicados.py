def eliminar_repeticiones(lista):
    return list(dict.fromkeys(lista))
lista_original=[1,2,2,3,4,4,5.5,6]
nueva_lista=[1,2,3,4,5,6]
eliminar_repeticiones(lista_original)
print(nueva_lista) #Salida:[1,2,3,4,5,6]
