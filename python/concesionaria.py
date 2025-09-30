class auto:
    def __init__(self,marca,modelo,anio,combustible, precio):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.combustible=combustible
        self.precio=precio
        self.estado="disponible"
class concesionario:
    def __init__(self):
        self.inventario=[]
        self.vendidos=[]
    def add_auto(self,auto):
        self.inventario.append(auto)
    def listar(self):
        for i in self.inventario:
            print(i.)
        

            
        