from Modelos.Almacenista import Almacenista
from Repositorios.RepositorioAlmacenista import RepositorioAlmacenista


class ControladorAlmacenista():

    def __init__(self):
        self.repositorioAlmacenista = RepositorioAlmacenista()
        print("Creando ControladorAlmacenista")


    def index(self):
        return self.repositorioAlmacenista.findAll()

    def create(self,infoAlmacenista):
        nuevoAlmacenista=Almacenista(infoAlmacenista)
        return self.repositorioAlmacenista.save(nuevoAlmacenista)

    def show(self,id):
        elAlmacenista=Almacenista(self.repositorioAlmacenista.findById(id))
        return elAlmacenista.__dict__

    def update(self, id, infoAlmacenista):

        almacenistaActual = Almacenista(self.repositorioAlmacenista.findById(id))
        almacenistaActual.cedula = infoAlmacenista["cedula"]
        almacenistaActual.nombre = infoAlmacenista["nombre"]
        almacenistaActual.apellido = infoAlmacenista["apellido"]
        return self.repositorioAlmacenista.save(almacenistaActual)

    def delete(self,id):
        return self.repositorioAlmacenista.delete(id)