from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorAlmacenista import ControladorAlmacenista
from Controladores.ControladorProducto import ControladorProducto
from Controladores.ControladorProveedor import ControladorProveedor
from Controladores.ControladorInventario import ControladorInventario
from Controladores.ControladorInventarioProductos import ControladorInventarioProducto

app = Flask(__name__)
cors = CORS(app)

miControladorAlmacenista = ControladorAlmacenista()
miControladorProducto = ControladorProducto()
miControladorProveedor = ControladorProveedor()
miControladorInventario = ControladorInventario()
miControladorInventarioProducto = ControladorInventarioProducto()

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


@app.route("/almacenistas", methods=['GET'])
def getAlmacenistas():
    json = miControladorAlmacenista.index()
    return jsonify(json)


@app.route("/almacenistas", methods=['POST'])
def crearAlmacenista():
    data = request.get_json()
    json = miControladorAlmacenista.create(data)
    return jsonify(json)


@app.route("/almacenistas/<string:id>", methods=['GET'])
def getAlmacenista(id):
    json = miControladorAlmacenista.show(id)
    return jsonify(json)


@app.route("/almacenistas/<string:id>", methods=['PUT'])
def modificarAlmacenista(id):
    data = request.get_json()
    json = miControladorAlmacenista.update(id, data)
    return jsonify(json)


@app.route("/almacenistas/<string:id>", methods=['DELETE'])
def eliminarAlmacenista(id):
    json = miControladorAlmacenista.delete(id)
    return jsonify(json)


########################### Servicios Productos #####################

@app.route("/productos", methods=['GET'])
def getProductos():
    json = miControladorProducto.index()
    return jsonify(json)


@app.route("/productos/<string:id>", methods=['GET'])
def getProducto(id):
    json = miControladorProducto.show(id)
    return jsonify(json)


@app.route("/productos", methods=['POST'])
def crearProducto():
    data = request.get_json()
    json = miControladorProducto.create(data)
    return jsonify(json)


@app.route("/productos/<string:id>", methods=['PUT'])
def modificarProducto(id):
    data = request.get_json()
    json = miControladorProducto.update(id, data)
    return jsonify(json)


@app.route("/productos/<string:id>", methods=['DELETE'])
def eliminarProducto(id):
    json = miControladorProducto.delete(id)
    return jsonify(json)


@app.route("/productos/<string:id>/proveedores/<string:id_proveedor>",methods=['PUT'])
def asignarproveedorAProducto(id, id_proveedor):
    json = miControladorProducto.asignarProveedor(id, id_proveedor)
    return jsonify(json)

#################proveedores#######################
@app.route("/proveedores", methods=['GET'])
def getProveedores():
    json = miControladorProveedor.index()
    return jsonify(json)


@app.route("/proveedores/<string:id>", methods=['GET'])
def getProveedor(id):
    json = miControladorProveedor.show(id)
    return jsonify(json)


@app.route("/proveedores/<string:id>/productos", methods=['GET'])
def getProductosProveedor(id):
    json = miControladorProveedor.getProductos(id)
    return jsonify(json)


@app.route("/proveedores", methods=['POST'])
def crearProveedor():
    data = request.get_json()
    json = miControladorProveedor.create(data)
    return jsonify(json)


@app.route("/proveedores/<string:id>", methods=['PUT'])
def modificarProveedor(id):
    data = request.get_json()
    json = miControladorProveedor.update(id, data)
    return jsonify(json)


@app.route("/proveedores/<string:id>", methods=['DELETE'])
def eliminarProveedor(id):
    json = miControladorProveedor.delete(id)
    return jsonify(json)

########################### Servicios Inventarios ##################################

@app.route("/inventarios", methods=['GET'])
def getInventarios():
    json = miControladorInventario.index()
    return jsonify(json)

@app.route("/inventario/<string:id>", methods=['GET'])
def getInventario(id):
    json = miControladorInventario.show(id)
    return jsonify(json)

@app.route("/inventarios/almacenista/<string:id_almacenista>", methods=['POST'])
def crearInventario(id_almacenista):
    data = request.get_json()
    json = miControladorInventario.create(data, id_almacenista)
    return jsonify(json)

@app.route("/inventarios/<string:id_inventarios>/almacenista/<string:id_almacenista>/producto/<string:id_producto>", methods=['PUT'])
def modificarInventario(id_inventario, id_almacenista, id_producto):
    data = request.get_json()
    json = miControladorInventario.update(id_inventario, data, id_almacenista, id_producto)
    return jsonify(json)

@app.route("/inventarios/<string:id_inventario>", methods=['DELETE'])
def eliminarInventario(id_inventario):
    json = miControladorInventario.delete(id_inventario)
    return jsonify(json)



########################### Servicios Inventario Productos ##################################

@app.route("/inventarioproductos", methods=['GET'])
def getInventariosProductos():
    json = miControladorInventarioProducto.index()
    return jsonify(json)

@app.route("/inventarioproductos/inventario/<string:id>", methods=['GET'])
def getInventarioProductos(id):
    json = miControladorInventarioProducto.show(id)
    return jsonify(json)

@app.route("/inventarioproductos/inventario/<string:id_inventario>/producto/<string:id_producto>", methods=['POST'])
def crearInventarioProductos(id_inventario,id_producto):
    data = request.get_json()
    json = miControladorInventarioProducto.create(data, id_inventario,id_producto)
    return jsonify(json)

@app.route("/inventarios/<string:id_inventarios>/almacenista/<string:id_almacenista>/producto/<string:id_producto>", methods=['PUT'])
def modificarInventarioProductos(id_inventario, id_almacenista, id_producto):
    data = request.get_json()
    json = miControladorInventarioProducto.update(id_inventario, data, id_almacenista, id_producto)
    return jsonify(json)

@app.route("/inventarioproductos/<string:id_inventario>", methods=['DELETE'])
def eliminarInventarioProductos(id_inventario):
    json = miControladorInventarioProducto.delete(id_inventario)
    return jsonify(json)


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
