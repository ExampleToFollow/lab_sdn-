import yaml

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




def cargar_datos(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)
# Menú principal
def imprimir_menu():
    print("\nSeleccione una opción:")
    print("1) Importar")
    print("2) Exportar")
    print("3) Cursos")
    print("4) Alumnos")
    print("5) Servidores")
    print("6) Políticas")
    print("7) Conexiones")
    print("8) Salir")
def imprimir_menu_crud():
    print("\nSeleccione una opción:")
    print("1) Crear")
    print("2) Listar")
    print("3) Mostrar detalle")
    print("4) Actualizar")
    print("5) Borrar")
    print("6) salir")
    print("")

#CRUD DE CURSOS


def listar_curso(data):
    print("Cursos registrados:")
    for curso in data["cursos"]:
        print(f"- {curso['nombre']} (Código: {curso['codigo']}, Estado: {curso['estado']})")

def mostrar_detalle_curso():
    print("")

def actualizar_curso():
    print("")

def delete_curso():
    print("")

def crear_curso():
    print("")

#Hola
def menu():
    filename = ""
    data  =  ""
    print("###########################################")
    print("Network Policy Manager de la UPSM")
    print("###########################################")
    while True:
        imprimir_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1" : 
            print("Ingresé el nombre del archivo q desea importar")
            filename = input(">>")
            data = cargar_datos(filename)
        elif opcion =="2" :
            if(data!=""):
                print("Todavía no se habilita esta opción x,d")
            else:
                print("Debe importar datos")
        elif opcion =="3" : 
            #Cursos
            if(data!=""):
                print("")
            else:
                print("Debe importar datos")
        elif opcion =="4" : 
            if(data!=""):
                print("")
            else:
                print("Debe importar datos")
        elif opcion =="5" : 
            if(data!=""):
                print("")
            else:
                print("Debe importar datos")
        elif opcion =="6" : 
            if(data!=""):
                print("")
            else:
                print("Debe importar datos")
        elif opcion =="7" : 
            if(data!=""):
                print("")
            else:
                print("Debe importar datos")
        elif opcion =="8" : 
            break
        else:
            print("Ingresa algo correcto")
            continue
            

if __name__ == "__main__":
    bd = "database.yaml"  
    datos = cargar_datos(bd)
    menu()
