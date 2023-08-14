from Modelos.Inventario import Inventario
from Modelos.Almacenista import Almacenista
from Modelos.Producto import Producto
from Repositorios.RepositorioInventario import RepositorioInventario
from Repositorios.RepositorioAlmacenista import RepositorioAlmacenista
from Repositorios.RepositorioProducto import RepositorioProducto


class ControladorInventario():

    def __init__(self):
        self.repositorioInventario = RepositorioInventario()
        self.repositorioAlmacenista = RepositorioAlmacenista()
        self.repositorioProducto = RepositorioProducto()

    def index(self):
        return self.repositorioInventario.findAll()
    """
    Asignacion estudiante y materia a inscripción
    """
    def create(self, infoInventario, id_almacenista):
        nuevoInventario = Inventario(infoInventario)
        elAlmacenista = Almacenista(self.repositorioAlmacenista.findById(id_almacenista))
        #elProducto = Producto(self.repositorioProducto.findById(id_producto))
        nuevoInventario.almacenista = elAlmacenista
        #nuevoInventario.producto = elProducto
        return self.repositorioInventario.save(nuevoInventario)

    def show(self, id):
        elInventario = Inventario(self.repositorioInventario.findById(id))
        elInventario.almacenista=elInventario.almacenista["_id"]
        return elInventario.__dict__
    """
    Modificación de inscripción (estudiante y materia)
    """
    def update(self, id, infoInventario):
        elInventario = Inventario(self.repositorioInventario.findById(id))
        elInventario.ano = infoInventario["ano"]
        #elInventario.cantidad = infoInventario["cantidad"]
        elInventario.mes = infoInventario["mes"]
        elInventario.nombre_inventario = infoInventario["nombre_inventario"]
        elInventario.almacenista=Almacenista(self.repositorioAlmacenista.findById(infoInventario["almacenista"]))
        return self.repositorioInventario.save(elInventario)

    def delete(self, id):
        return self.repositorioInventario.delete(id)