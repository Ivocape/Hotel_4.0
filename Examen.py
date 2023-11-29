import numpy as np
###############################################################3
# Por alguna razon no me esta funcionando bien el borrar los nodos con suma impar
# Invertir la lista funciona bien

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.proxNode = None

class ListaCircularEnlazada:
    def __init__(self):
        self.head = None

    def append(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.proxNode != None:
                actual = actual.proxNode
            actual.proxNode = nuevo_nodo    

        return

    def imprimir(self):
        if self.head is None:
            print("La lista está vacía")
            return

        actual = self.head
        while actual != None:
                print(actual.dato)
                actual = actual.proxNode
            

    def sumarContenido(self):
        if self.head is None:
            print("La lista está vacía")
            return
        
        actual = self.head
        
        self.suma_actual = actual.dato.sum()

        while actual != None:
            
            if self.suma_actual % 2 != 0:  # Si la suma es impar, se elimina el nodo
                if actual == self.head:  # Si es el primer nodo
                    self.head = actual.proxNode
                    actual = actual.proxNode
                    self.suma_actual = actual.dato.sum()

                    print("Se ha eliminado el primer nodo")

                else:  # Si es un nodo intermedio
                    actual.proxNode = actual.proxNode
                    actual = actual.proxNode
                    self.suma_actual = actual.dato.sum()
                    print("Se ha eliminado un nodo intermedio")
            actual = actual.proxNode
        
        

    def invertirLista(self):
        if self.head is None:
            print("La lista está vacía")
            return

        prev = None
        actual = self.head
        siguiente = None
        while actual:
            siguiente = actual.proxNode
            actual.proxNode = prev
            prev = actual
            actual = siguiente
            if actual == self.head:  # Si se completa el ciclo
                break

        self.head = prev  # Se establece el nuevo head como el último nodo invertido

        print("La lista ha sido invertida") 
            
listaMatriz = ListaCircularEnlazada()

while True:
    print("1. Ingresar números para una matriz 3x3")
    print("2. Obtener la suma de todas las matrices y eliminar nodos con suma impar")
    print("3. Mostrar la lista de matrices")
    print("4. Invertir la lista")
    print("5. Salir")
    
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        matriz = np.zeros((3, 3), dtype=int)
        for i in range(3):
            for j in range(3):
                matriz[i, j] = int(input(f"Ingrese un número para la posición [{i}][{j}]: "))
        listaMatriz.append(matriz)
    
    elif opcion == "2":
        listaMatriz.sumarContenido()
    
    elif opcion == "3":
        listaMatriz.imprimir()
    
    elif opcion == "4":
        listaMatriz.invertirLista()
    
    elif opcion == "5":
        break

