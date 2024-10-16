class Venta:
    def __init__(self, id_venta=None, fecha=None, cliente=None):
        self.__id_venta = id_venta
        self.__fecha = fecha
        self.__cliente = cliente
        self.__productos = []
        self.__total = 0.0

    # Setter para el id_venta
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    # Getter para el id_venta
    def get_id_venta(self):
        return self.__id_venta

    # Setter para productos
    def set_productos(self, productos):
        self.__productos = productos
        self.__total = sum(p['cantidad'] * p['precio_unitario'] for p in productos)

    # Método para mostrar detalles
    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print("Productos:")
        for producto in self.__productos:
            print(f"{producto['producto']}: {producto['cantidad']} unidades, Precio unitario: {producto['precio_unitario']}")
        print(f"Total: ${self.__total:.2f}")
