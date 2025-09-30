class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        if self.stock + cantidad < 0:
            print(f"No hay suficiente stock para {self.nombre}")
            return False
        self.stock += cantidad
        return True
class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = []

    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            print(f"Se agregaron {cantidad} x {producto.nombre} al carrito.")
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")

    def eliminar_producto(self, producto):
        for item in self.carrito:
            if item[0] == producto:
                self.carrito.remove(item)
                print(f"{producto.nombre} eliminado del carrito.")
                return
        print(f"{producto.nombre} no estaba en el carrito.")

    def ver_carrito(self):
        if not self.carrito:
            print("El carrito está vacío.")
        else:
            print("Carrito de compras:")
            for producto, cantidad in self.carrito:
                print(f" - {cantidad} x {producto.nombre} (${producto.precio} c/u)")


class Orden:
    contador_ordenes = 1

    def __init__(self, cliente, carrito):
        self.numero_orden = Orden.contador_ordenes
        Orden.contador_ordenes += 1
        self.cliente = cliente
        self.productos = carrito
        self.valor_total = sum(p.precio * c for p, c in carrito)

    def confirmar_compra(self):
        for producto, cantidad in self.productos:
            producto.actualizar_stock(-cantidad)
        print(f"\nOrden #{self.numero_orden} confirmada.")
        print(f"Cliente: {self.cliente.nombre} ({self.cliente.correo})")
        print("Productos adquiridos:")
        for producto, cantidad in self.productos:
            print(f" - {cantidad} x {producto.nombre} (${producto.precio} c/u)")
        print(f"Total: ${self.valor_total}\n")




# Crear productos
p1 = Producto("Laptop", "Electrónica", 2500, 5)
p2 = Producto("Auriculares", "Accesorios", 200, 10)
p3 = Producto("Mouse", "Accesorios", 100, 8)

# Crear cliente
cliente1 = Cliente("Fabian", "fabian@mail.com")

# Cliente agrega productos
cliente1.agregar_producto(p1, 1)
cliente1.agregar_producto(p2, 2)
cliente1.ver_carrito()

# Confirmar orden
orden1 = Orden(cliente1, cliente1.carrito)
orden1.confirmar_compra()

# Mostrar stock actualizado
print("\nStock después de la compra:")
print(p1)
print(p2)
print(p3)
        

        
        