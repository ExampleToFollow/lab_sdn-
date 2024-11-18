class Alumno:
    def __init__(self, nombre, codigo, mac):
        self.nombre = nombre
        self.codigo = codigo
        self.mac = mac

class Servicio:
    def __init__(self, nombre, protocolo, puerto):
        self.nombre = nombre
        self.protocolo = protocolo
        self.puerto = puerto

class Servidor:
    def __init__(self, nombre, direccion_ip, servicios=None):
        self.nombre = nombre
        self.direccion_ip = direccion_ip
        self.servicios = []

class Curso:
    def __init__(self, nombre, estado,alumnos, servidores):
        self.nombre = nombre
        self.estado = estado
        self.alumnos = alumnos
        self.servidores = servidores
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)
    def remover_alumno(self, alumno):
        self.alumnos = [a for a in self.alumnos if a.nombre != alumno.nombre]
    def añadir_servidor(self, servidor):
        self.servidores.append(servidor)