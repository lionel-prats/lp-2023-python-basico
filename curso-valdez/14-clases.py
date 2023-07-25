class Restaurant:
    def agregar_restaurant(self, nombre):
        self.nombre = nombre # Atributo
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")

# Instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurant("Pizzería Mexico") # seteo el atributo nombre del objeto
restaurant.mostrar_informacion() # imprime el atributo nombre del objeto

restaurant2 = Restaurant()
restaurant2.agregar_restaurant("Pizzería Banchero")
restaurant2.mostrar_informacion()

print("----------------------------------------")

print(f"Nombre Restaurant: {restaurant.nombre}")
print(f"Nombre Restaurant2: {restaurant.nombre}")