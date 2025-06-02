from flask import Flask, request, jsonify
from services import procesar_pago, realizar_compra

app = Flask(__name__)

@app.route('/pagar', methods=['POST'])
def pagar():
    numero_tarjeta = request.form.get('numero_tarjeta')
    monto = float(request.form.get('monto'))
    nombre = request.form.get('nombre')
    codigo_CVV = request.form.get('codigo_CVV')

    resultado = procesar_pago(numero_tarjeta, monto, nombre, codigo_CVV)
    return jsonify({"resultado": resultado})

@app.route('/comprar', methods=['POST'])
def comprar():
    id_producto = request.form.get('id_producto')
    precio = float(request.form.get('precio'))
    numero_productos = int(request.form.get('numero_productos'))
    total = float(request.form.get('total'))

    resultado = realizar_compra(id_producto, precio, numero_productos, total)
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
