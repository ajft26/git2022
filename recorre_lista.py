lista_recorrer = [{"name":"Alfonso","Value":1000},{"name":"Hugo","Value":2000},{"name":"Memo","Value":4500},{"name":"Eve","Value":5000}]
lista_recorrer.sort(key= lambda p: p["Value"], reverse = True)
print(lista_recorrer)