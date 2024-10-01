def sumar_numeros_pares(lista):
    return sum(num for num in lista if num %2==0)

lista=[1,2,3,4,5,6,7,8,9,10]
resultado=sumar_numeros_pares(lista)
print(resultado)#Salida:30


