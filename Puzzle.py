from arbol import Nodo
"""Implementa el algoritmo de búsqueda en amplitud (BFS) para encontrar la solución al problema del puzzle."""
def buscar_solucion_BFS(estado_inicial, solucion):
    """Inicialización de variables."""
    solucionado = False # Una variable almacenada para indicar si se encontró la solución.
    nodos_visitados = [] # Guarda los nodos que ya han sido visitados.
    nodos_frontera = [] # Guarda los nodos que están en la "cola" para ser explorados.
    
    nodo_inicial = Nodo(estado_inicial) # Crea un nodo con el estado inicial.
    nodos_frontera.append(nodo_inicial) # Añade el nodo inicial a la lista de nodos frontera.

    """
    Mientras no se haya encontrado la solución y haya nodos en la frontera:
        - Extraer el primer nodo de la frontera. (nodos_frontera.pop(0))
        - Añade el nodo a la lista de nodos visitados.
        - Si el nodo contiene la  solución, retorna el nodo
        - Si no, genera los nodos hijos aplicando los operadores (izquierda, central y derecho del codigo de "arbol.py")
        - Añade los nodos hijos a la lista de nodos frontera, si no han sido visitados o ni estan en la lista de nodos frontera.

    Si no encuentra la solución, retorna "None".
    """
    while not solucionado and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0) # SE MODIFICA PARA CONVERTIRLO DE FIFO A LIFO (se elimina o se quita el cero)
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            # Solución encontrada
            solucionado = True
            return nodo
        else:
            # Expandir nodos hijos
            dato_nodo = nodo.get_datos()
            
            """Intercambia el primer y el segundo valor de la lista."""
            # Operador Izquierdo (Necesario para llegar al siguiente estado correcto)
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            hijo_izquierdo.set_padre(nodo)
            if not hijo_izquierdo.en_lista(nodos_visitados) \
               and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)

            """Intercambia el segundo y el tercer valor de la lista."""
            # Operador Central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            hijo_central.set_padre(nodo)
            if not hijo_central.en_lista(nodos_visitados) \
               and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)

            """Intercambia el tercer y el cuarto valor de la lista."""
            # Operador Derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo)
            hijo_derecho.set_padre(nodo)
            if not hijo_derecho.en_lista(nodos_visitados) \
               and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)

    return None  # En caso de no encontrar solución

"""Ejecución del algoritmo y muestra el resultado."""
if __name__ == "__main__":

    """Define el estado inicial y la solución."""
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]

    """Llama a la función de "búsqueda_solución_BFS" para encontrar la solución."""
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)

    """
    Si se encuantre la solución:
        - Reconstruye la secuencia de estados desde el nodo solución hasta el nodo inicial.
        - Muestra la secuencia en orden correcto (usando "reverse()").
    
    Si no encuenra la solución, muestra un mensaje de advertencia, indicando que no se encontro una solución.
    """
    if nodo_solucion is not None:
        # Mostrar resultado
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()  # Para mostrar la secuencia completa
        print("Solución encontrada:", resultado)
    else:
        print("No se encontró una solución.")
