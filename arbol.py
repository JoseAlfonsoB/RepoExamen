class Nodo:
    """CONSTRUCTOR DE LA CLASE NODO"""
    def __init__(self, datos, hijos=None):
        """ Inicializa los datos del nodo."""
        self.datos = datos #Almacena los datos del nodo.
        self.hijos = [] # Es una lista que almacena los nodos hijos. (Se inicializa como vacía).
        self.padre = None # Almacena el nodo padre. (Se inicializa como None).
        self.costo = 0  # Inicializado en 0 para evitar problemas con operaciones numéricas.
        self.set_hijos(hijos) # Se manda a llamar a la función set_hijos para agregar los nodos hijos.

        """
        EJEMPLO:
            nodo = Nodo("A") # Crea un nodo con el dato "A" y sin hijos.
        """

    """
    Asigna una lista de nodos hijos al nodo actual.
    """
    def set_hijos(self, hijos):
        if hijos is not None and isinstance(hijos, list):
            self.hijos = hijos
            for h in hijos:
                if isinstance(h, Nodo):
                    h.padre = self
                else:
                    print(f"Advertencia: El hijo {h} no es una instancia de Nodo.")
        else:
            self.hijos = []

            """
            EJEMPLO:
                hijo1 = Nodo("B")
                hijo2 = Nodo("C")
                nodo.set_hijos([hijo1, hijo2])  # Asigna hijo1 y hijo2 como hijos del nodo.
            """

    def get_hijos(self):
        return self.hijos

    def set_datos(self, datos):
        self.datos = datos

    """Devuelve los datos que almacena el nodo."""
    def get_datos(self):
        return self.datos
    """Asigna una costo al nodo"""
    def set_costo(self, costo):
        if isinstance(costo, (int, float)):
            self.costo = costo
        else:
            print(f"Advertencia: El costo debe ser un número, se recibió {type(costo)}")

    def get_costo(self):
        return self.costo

    def set_padre(self, padre):
        if isinstance(padre, Nodo):
            self.padre = padre
        else:
            print(f"Advertencia: El padre debe ser una instancia de Nodo, se recibió {type(padre)}")

    def get_padre(self):
        return self.padre

    def igual(self, nodo):
        if isinstance(nodo, Nodo):
            return self.get_datos() == nodo.get_datos()
        return False

    def en_lista(self, lista_nodos):
        for n in lista_nodos:
            if self.igual(n):
                return True
        return False

    def __str__(self):
        return str(self.get_datos())
