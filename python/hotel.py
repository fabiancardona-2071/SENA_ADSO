from datetime import datetime

class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo  # sencilla, doble, suite
        self.estado = "disponible"

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}) - {self.estado}"


class Huesped:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def __str__(self):
        return f"Huésped: {self.nombre}, Documento: {self.documento}"


class Reserva:
    contador = 1  # para generar IDs únicos

    def __init__(self, huesped, habitacion, fecha_ingreso, fecha_salida):
        self.numero = Reserva.contador
        Reserva.contador += 1
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        self.fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d")

    def __str__(self):
        return (f"Reserva {self.numero}: {self.huesped.nombre} en "
                f"Habitación {self.habitacion.numero} "
                f"del {self.fecha_ingreso.date()} al {self.fecha_salida.date()}")


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def realizar_reserva(self, huesped, numero_habitacion, fecha_ingreso, fecha_salida):
        habitacion = next((h for h in self.habitaciones if h.numero == numero_habitacion), None)
        if not habitacion:
            print("Habitación no encontrada.")
            return None

        # Verificar solapamiento de fechas con reservas existentes
        for reserva in self.reservas:
            if reserva.habitacion.numero == numero_habitacion:
                if not (datetime.strptime(fecha_salida, "%Y-%m-%d") <= reserva.fecha_ingreso or
                        datetime.strptime(fecha_ingreso, "%Y-%m-%d") >= reserva.fecha_salida):
                    print("La habitación ya está reservada en ese período.")
                    return None

        nueva_reserva = Reserva(huesped, habitacion, fecha_ingreso, fecha_salida)
        self.reservas.append(nueva_reserva)
        huesped.agregar_reserva(nueva_reserva)
        habitacion.estado = "ocupada"
        print(f"Reserva realizada con éxito: {nueva_reserva}")
        return nueva_reserva

    def cancelar_reserva(self, numero_reserva):
        reserva = next((r for r in self.reservas if r.numero == numero_reserva), None)
        if reserva:
            self.reservas.remove(reserva)
            reserva.habitacion.estado = "disponible"
            print(f"Reserva {numero_reserva} cancelada.")
        else:
            print("Reserva no encontrada.")

    def consultar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
        for reserva in self.reservas:
            print(reserva)




if __name__ == "__main__":
    hotel = Hotel("Hotel Python")

    # Agregar habitaciones
    hotel.agregar_habitacion(Habitacion(101, "sencilla"))
    hotel.agregar_habitacion(Habitacion(102, "doble"))

    # Crear huéspedes
    huesped1 = Huesped("Carlos López", "123456")
    huesped2 = Huesped("Ana Gómez", "789012")

    # Realizar reservas
    hotel.realizar_reserva(huesped1, 101, "2025-09-25", "2025-09-28")
    hotel.realizar_reserva(huesped2, 101, "2025-09-26", "2025-09-27")  # debe fallar por solapamiento
    hotel.realizar_reserva(huesped2, 102, "2025-09-26", "2025-09-27")

    # Consultar reservas
    hotel.consultar_reservas()

    # Cancelar una reserva
    hotel.cancelar_reserva(1)

    # Consultar de nuevo
    hotel.consultar_reservas()
        