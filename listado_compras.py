# Crear una lista vacía llamada listado_compras
listado_compras =[]

# Crear una funcion llamada agregar_lista que tiene un parametro llamado elemento
def agregar_lista(elemento):
    # Agregar el elemento a la lista
    listado_compras.append(elemento)
    # Notificar al usuario que un elemento fue agregado a la lista
    # Y mostrar el numero de elementos agregados a la lista
    print("¡Agregado! La lista tiene {} elementos.".format(len(listado_compras)))


def mostrar_ayuda():
    print("Qué deberíamos elegir en el supermercado?")
    print("""
Ingresa 'TERMINADO' cuando termines de agregar elementos
Ingresa 'AYUDA' para ingresar a ésta ayuda
Ingresa 'MOSTRAR' para ver tu lista actual
""")


# Definir una funcion para mostrar_lista
def mostrar_lista():
    print("Esta es la lista: ")
    for indice, elemento in enumerate(listado_compras, start=1):
        print("{}, {}".format(indice, elemento))

mostrar_ayuda()
while True:
    nuevo_item = input(">  ")

    if nuevo_item == 'TERMINADO':
        break
    elif nuevo_item == 'AYUDA':
        mostrar_ayuda()
        continue
    # Habilitar el comando de MOSTRAR para mostrar la lista. Actualiza el texto de AYUDA
    # Asegurate de correrlo
    elif nuevo_item == 'MOSTRAR':
        mostrar_lista()
        continue
    # Llamar agregar_lista con un nuevo elemento como argumento
    agregar_lista(nuevo_item)


mostrar_lista()