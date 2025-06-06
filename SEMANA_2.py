class Vehiculo:
    def __init__(self, marca, velocidad):
        self.__marca = marca          # Encapsulación (atributo privado)
        self.__velocidad = velocidad

    def mostrar_info(self):
        print(f"Vehículo de marca: {self.__marca}")
        print(f"Velocidad máxima: {self.__velocidad} km/h")

    def tipo(self):
        return "Vehículo genérico"   # Polimorfismo


class Auto(Vehiculo):
    def __init__(self, marca, velocidad, puertas):
        super().__init__(marca, velocidad)
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de puertas: {self.puertas}")

    def tipo(self):                  # Polimorfismo
        return "Auto"


class Bicicleta(Vehiculo):
    def __init__(self, marca, velocidad, tipo_bici):
        super().__init__(marca, velocidad)
        self.tipo_bici = tipo_bici

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de bicicleta: {self.tipo_bici}")

    def tipo(self):                  # Polimorfismo
        return "Bicicleta"


# Abstracción en acción: usamos los métodos sin preocuparnos de la implementación interna
vehiculos = [
    Auto("Toyota", 180, 4),
    Bicicleta("Giant", 45, "Montaña")
]

for v in vehiculos:
    print("\n--- Información del vehículo ---")
    v.mostrar_info()
    print("Tipo:", v.tipo())
