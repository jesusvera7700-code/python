# 1. Definir la plantilla (Clase)
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo
        self.raza = raza      # Atributo

    def ladrar(self):         # Método
        return "¡Guau!"

# 2. Crear el objeto (Instanciar)
mi_perro = Perro("Firulais", "Labrador")

# 3. Usar el objeto
print(mi_perro.nombre)  # Imprime: Firulais
print(mi_perro.ladrar()) # Imprime: ¡Guau!
