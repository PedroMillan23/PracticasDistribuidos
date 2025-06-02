# services.py

def procesar_pago(numero_tarjeta, monto, nombre, codigo_CVV):
    try:
        monto = float(monto)
    except ValueError:
        return False

    if len(str(numero_tarjeta)) >= 13 and len(str(codigo_CVV)) in [3, 4] and monto > 0:
        return True
    return False

def realizar_compra(id_producto, precio, numero_productos, total):
    try:
        precio = float(precio)
        total = float(total)
        numero_productos = int(numero_productos)
    except ValueError:
        return False

    if precio * numero_productos == total and numero_productos > 0:
        return True
    return False
