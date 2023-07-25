# el constructor de una clase es un metodo que se ejecuta automaticamente cuando se instancia la clase
class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre 
        self.categoria = categoria 
        self.precio = precio 

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}. Categoría: {self.categoria}. Precio: ${self.precio}")

restaurant = Restaurant("Milanesa a caballo con guarnición", "minutas", 1800)
restaurant.mostrar_informacion() 

restaurant2 = Restaurant("Sopa inglesa", "postre", 800)
restaurant2.mostrar_informacion()
