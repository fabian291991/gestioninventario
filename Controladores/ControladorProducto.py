from Repositorios.RepositorioProducto import RepositorioProducto
from Repositorios.RepositorioProveedor import RepositorioProveedor
from Modelos.Producto import Producto
from Modelos.Proveedor import Proveedor


class ControladorProducto:

    def __init__(self):
        self.repositorioProducto = RepositorioProducto()
        self.repositorioProveedor = RepositorioProveedor()

    def index(self):
        return self.repositorioProducto.findAll()

    def create(self,infoProducto):
        nuevoProducto=Producto(infoProducto)
        return self.repositorioProducto.save(nuevoProducto)

    def show(self,id):
        elProducto=Producto(self.repositorioProducto.findById(id))
        return elProducto.__dict__

    def update(self, id, infoProducto):

        productoActual = Producto(self.repositorioProducto.findById(id))
        productoActual.precio = infoProducto["precio"]
        productoActual.referencia = infoProducto["referencia"]
        productoActual.marca = infoProducto["marca"]
        productoActual.talla = infoProducto["talla"]
        return self.repositorioProducto.save(productoActual)

    def delete(self,id):
        return self.repositorioProducto.delete(id)
    def asignarProveedor(self, id, id_proveedor):
        productoActual = Producto(self.repositorioProducto.findById(id))
        proveedorActual = Proveedor(self.repositorioProveedor.findById(id_proveedor))
        productoActual.proveedor = proveedorActual
        return self.repositorioProducto.save(productoActual)

