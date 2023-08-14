from bson import ObjectId

from Modelos.Inventario import Inventario
from Modelos.Almacenista import Almacenista
from Modelos.InventarioProducto import InventarioProducto
from Modelos.Producto import Producto
from Repositorios.RepositorioInventario import RepositorioInventario
from Repositorios.RepositorioAlmacenista import RepositorioAlmacenista
from Repositorios.RepositorioInventarioProducto import RepositorioInventarioProducto
from Repositorios.RepositorioProducto import RepositorioProducto


class ControladorInventarioProducto():

    def __init__(self):
        self.repositorioInventario = RepositorioInventario()
        self.repositorioInventarioProducto = RepositorioInventarioProducto()
        self.repositorioProducto = RepositorioProducto()

    def index(self):
        return self.repositorioInventarioProducto.findAll()
    """
    Asignacion estudiante y materia a inscripción
    """
    def create(self, infoInventario):
        nuevoInventarioProducto = InventarioProducto(infoInventario)
        producto = Producto(self.repositorioProducto.findById(infoInventario["producto"]))
        inventario = Inventario(self.repositorioInventario.findById(infoInventario["inventario"]))
        nuevoInventarioProducto.inventario = inventario
        nuevoInventarioProducto.producto = producto
        return self.repositorioInventarioProducto.save(nuevoInventarioProducto)

    def show(self, id):
        elInventario = self.repositorioInventarioProducto.query({"inventario.$id":ObjectId(id)})
        return elInventario
    """
    Modificación de inscripción (estudiante y materia)
    """
    def update(self, id, infoInventario, id_almacenista, id_producto):
       return "none"

    def delete(self, id):
        return self.repositorioInventarioProducto.delete(id)