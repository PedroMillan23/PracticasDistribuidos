import requests
from tkinter import *

def realizar_pago():
    data = {
        "numero_tarjeta": entry_tarjeta.get(),
        "monto": entry_monto.get(),
        "nombre": entry_nombre.get(),
        "codigo_CVV": entry_cvv.get()
    }
    r = requests.post("http://localhost:5000/pagar", data=data)
    resultado = r.json().get("resultado")
    if resultado:
        resultado_pago.config(text="TRANSACCIÓN EXITOSA", fg="green")
    else:
        resultado_pago.config(text="FALLÓ LA TRANSACCIÓN", fg="red")

def realizar_compra():
    data = {
        "id_producto": entry_producto.get(),
        "precio": entry_precio.get(),
        "numero_productos": entry_cantidad.get(),
        "total": entry_total.get()
    }
    r = requests.post("http://localhost:5000/comprar", data=data)
    resultado = r.json().get("resultado")
    if resultado:
        resultado_compra.config(text="COMPRA EXITOSA", fg="green")
    else:
        resultado_compra.config(text="FALLÓ LA COMPRA", fg="red")

root = Tk()
root.title("Cliente Transacción")

# Sección de pago
Label(root, text="Pago").grid(row=0, column=0, columnspan=2)
Label(root, text="Tarjeta:").grid(row=1, column=0)
entry_tarjeta = Entry(root)
entry_tarjeta.grid(row=1, column=1)

Label(root, text="Monto:").grid(row=2, column=0)
entry_monto = Entry(root)
entry_monto.grid(row=2, column=1)

Label(root, text="Nombre:").grid(row=3, column=0)
entry_nombre = Entry(root)
entry_nombre.grid(row=3, column=1)

Label(root, text="CVV:").grid(row=4, column=0)
entry_cvv = Entry(root)
entry_cvv.grid(row=4, column=1)

Button(root, text="Pagar", command=realizar_pago).grid(row=5, column=0, columnspan=2)
resultado_pago = Label(root, text="Resultado:")
resultado_pago.grid(row=6, column=0, columnspan=2)

# Sección de compra
Label(root, text="\nCompra").grid(row=7, column=0, columnspan=2)
Label(root, text="ID Producto:").grid(row=8, column=0)
entry_producto = Entry(root)
entry_producto.grid(row=8, column=1)

Label(root, text="Precio:").grid(row=9, column=0)
entry_precio = Entry(root)
entry_precio.grid(row=9, column=1)

Label(root, text="Cantidad:").grid(row=10, column=0)
entry_cantidad = Entry(root)
entry_cantidad.grid(row=10, column=1)

Label(root, text="Total:").grid(row=11, column=0)
entry_total = Entry(root)
entry_total.grid(row=11, column=1)

Button(root, text="Comprar", command=realizar_compra).grid(row=12, column=0, columnspan=2)
resultado_compra = Label(root, text="Resultado:")
resultado_compra.grid(row=13, column=0, columnspan=2)

root.mainloop()
