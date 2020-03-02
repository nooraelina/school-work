def sum(lista):
    summa = 0


    
    if len(lista) == 0:
        return summa
    for i in lista:
        if i % 2 == 0:
            summa += i
    lista.pop(0)
    return sum(lista)

listaaa = [1,2,4,3,7,54]
print(sum(listaaa))