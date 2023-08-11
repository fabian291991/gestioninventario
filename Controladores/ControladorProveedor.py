from Repositorios.RepositorioProveedor import RepositorioProveedor
from Modelos.Proveedor import Proveedor



class ControladorProveedor:

    def __init__(self):
        self.repositorioProveedor = RepositorioProveedor()

    def index(self):
        return self.repositorioProveedor.findAll()

    def create(self,infoProveedor):
        nuevoProveedor=Proveedor(infoProveedor)
        return self.repositorioProveedor.save(nuevoProveedor)

    def show(self,id):
        elProveedor=Proveedor(self.repositorioProveedor.findById(id))
        return elProveedor.__dict__

    def update(self, id, infoProveedor):

        proveedorActual = Proveedor(self.repositorioProveedor.findById(id))
        proveedorActual.nombre = infoProveedor["nombre"]
        proveedorActual.nit_proveedor = infoProveedor["nit_proveedor"]
        proveedorActual.correo = infoProveedor["correo"]
        proveedorActual.telefono = infoProveedor["telefono"]
        return self.repositorioProveedor.save(proveedorActual)

    def delete(self,id):
        return self.repositorioProveedor.delete(id)