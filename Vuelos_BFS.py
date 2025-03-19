# Vuelos con Búsqueda en Amplitud
from arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)
    
    while not solucionado and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)  # Extrae el nodo de la frontera
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo  # Devuelve el nodo solución

        # Expandir los nodos hijos
        dato_nodo = nodo.get_datos()
        lista_hijos = []
        
        for un_hijo in conexiones.get(dato_nodo, []):  # Evita errores si la clave no está
            hijo = Nodo(un_hijo)
            hijo.set_padre(nodo)  # Asigna el nodo padre
            lista_hijos.append(hijo)

            if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo)

if __name__ == "__main__":
    conexiones = {
        'CDMX': ['SLP', 'MEXICALI', 'CHIHUAHUA'],
        'SAPOPAN': ['ZACATECAS', 'MEXICALI'],
        'GUADALAJARA': ['CHIAPAS'],
        'CHIAPAS': ['CHIHUAHUA'],
        'MEXICALI': ['SLP', 'SAPOPAN', 'CDMX', 'CHIHUAHUA', 'SONORA'],
        'SLP': ['CDMX', 'MEXICALI'],
        'ZACATECAS': ['SAPOPAN', 'SONORA', 'CHIHUAHUA'],
        'SONORA': ['ZACATECAS', 'MEXICALI'],
        'MICHOACAN': ['CHIHUAHUA'],
        'CHIHUAHUA': ['MICHOACAN', 'ZACATECAS', 'MEXICALI', 'CDMX'],
    }

    estado_inicial = 'CDMX'
    solucion = 'ZACATECAS'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)

    # Mostrar el resultado
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()
        print("Ruta encontrada:", resultado)
    else:
        print("No se encontró una ruta.")