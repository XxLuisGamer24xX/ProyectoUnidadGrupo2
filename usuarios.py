from abc import ABC, abstractmethod
class Usuarios():
    def __init__(self, cedula, nombre, apellido, correo, telefono, rol):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.rol = rol
class administrador(Usuarios):
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
class usuarioReporte(Usuarios):
    def __init__(self,callePrincipal,calleSecundario, tipoDeCaso, observaciones):
            self.callePrincipal = callePrincipal
            self.calleSecundario = calleSecundario
            self.tipoDeCaso = tipoDeCaso
            self.observaciones = observaciones
class Permisos(ABC):
    @abstractmethod
    def eliminarUsuario(self):
        pass
    @abstractmethod
    def editarUsuario(self):
        pass
    @abstractmethod
    def crearUsuario(self):
        pass
    @abstractmethod
    def editarReporte(self):
        pass
    @abstractmethod
    def eliminarReporte(self):
        pass
    @abstractmethod
    def registrase(self):
        pass
class administrador(Permisos):
    def eliminarUsuario(self):
        print("eliminar usuario")
    def editarUsuario(self):
        print("editar usuario")
    def crearUsuario(self):
        print("crear usuario")
    def editarReporte(self):
        print("editar reporte")
    def eliminarReporte(self):
        print("eliminar reporte") 
class secretaria():
    def eliminarUsuario(self):
        print("eliminar usuario")
    def editarUsuario(self):
        print("editar usuario")
class usuarioComún(Permisos):
    def registrase(self):
        return super().registrase()




