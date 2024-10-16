from classVenta import Venta

# Instancia de la clase Venta
venta = Venta()

# Asignar el ID de la venta
venta.set_id_venta(1)

# Datos ya dados para los productos
productos_datos = [
    {"producto": "Producto A", "cantidad": 2, "precio_unitario": 10.0},
    {"producto": "Producto B", "cantidad": 3, "precio_unitario": 20.50},
    {"producto": "Producto C", "cantidad": 1, "precio_unitario": 43.0}
]

# Asignar productos
venta.set_productos(productos_datos)

# Mostrar los detalles de la venta
venta.mostrar_detalle()
