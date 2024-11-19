import yaml
global alumnos_global
alumnos_global = []
global cursos_global
cursos_global = []
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
    def __init__(self, nombre, estado,alumnos, servidores,codigo):
        self.nombre = nombre
        self.estado = estado
        self.alumnos = alumnos
        self.servidores = servidores
        self.codigo = codigo
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)
    def remover_alumno(self, alumno):
        self.alumnos = [a for a in self.alumnos if a.nombre != alumno.nombre]
    def añadir_servidor(self, servidor):
        self.servidores.append(servidor)
class Servidor_DTO:
    def __init__(self, nombre, servicios_permitidos=None):
        self.nombre = nombre
        self.servicios_permitidos = servicios_permitidos
def cargar_datos(filename):
    with open('database.yaml','r') as f:
        data = yaml.safe_load(f)
        #Guardar a los alumnos:
        for curso in data.get('cursos',[]):
            alumnitos = []
            for a in curso.get("alumnos"):
                alumnitos.append(str(a))
            servidores = []
            for s in curso.get("servidores"):
                servicios_server= []
                for k in s.get('servicios_permitidos'):
                    servicios_server.append(k)
                servidores.append(Servidor_DTO(s.get('nombre'),servicios_server))
            cursos_global.append(Curso(curso.get('nombre'),curso.get('estado'),alumnitos, servidores,curso.get('codigo')))
        for alumno in data.get('alumnos',[]):
            alumnos_global.append(Alumno(alumno.get('nombre'),alumno.get('codigo'),alumno.get('mac')))
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
def menu_crud_cursos(filename):
    while True:
        imprimir_menu_crud()
        print("Ingrese una opcion: ")
        opcion_curso = input(">>")
        if opcion_curso == "1":
            crear_curso(filename)
        elif opcion_curso=="2":
            listar_curso()
        elif opcion_curso=="3":
            mostrar_detalle_curso()
        elif opcion_curso=="4":
            actualizar_curso()
        elif opcion_curso=="5":
            borrar_curso(filename)
        elif opcion_curso=="6":
            break
        else :
            print("Debes poner una opcion valida")

def listar_curso():
    for curso in cursos_global:
        print(f"- {curso.nombre} ")

def mostrar_detalle_curso():
    print("Ingrese el codigo del curso")
    codigo = input(">>")
    counter =0
    for i in cursos_global:
        if i.codigo == codigo:
            counter = counter+1
            print(f"- Nombre del curso : {i.nombre}")
            print(f"- Estado : {i.estado}")
            print(f"- Alumnos : ")
            for j in i.alumnos:
                for k in alumnos_global:
                    if j ==  k.codigo:
                        print(f"    -{k.nombre} ")
            print("Servidores: ")
            for j in i.servidores:
                print(f"     -{j.nombre}")
                print(f"     -Servicios_permitidos:")
                for k in j.servicios_permitidos:
                    print(f"                    -{k}")
    if counter==0:
        print("No se encontró algún curso con ese codigo")
def actualizar_curso():
    #Solo agrega o elimina alumno 
    while True:
        print("Ingresa el código del curso")
        code = input(">>")
        master_counter= 0
        for i in cursos_global:
            if i.codigo == code: 
                master_counter = master_counter +1
                print("Agregar (A) o Eliminar (E) un alumnos: ")
                opcion =  input(">> ")
                if opcion =="A" :
                    print("Ingresa el código del alumno a añadir:")
                    codigo = input(">>")
                    if(validate_alumno_existe_codigo(codigo)):
                        #Agregamos este codigo
                        i.alumnos.append(int(codigo))
                        print(f"Se agrego a alumno con codigo {codigo}")
                    else:
                        print("No existe este alumno")
                elif opcion =="E":
                    print("Ingresa el código del alumno a eliminar:")
                    codigo = input(">>")
                    ACounter= 0 
                    for j in i.alumnos:
                        if(j == int (codigo)):
                            ACounter = ACounter +1
                            i.alumnos.remove(int(codigo))
                    if(ACounter >0):
                        print("Se elimino correctamente al alumno")
                        break;    
                    else:
                        print("No se encontró al alumno")
                else:
                    print("debes ingresar una opcion valida")
                break
        if master_counter == 0:
            print("No se encontró ningun curso con ese codigo")
        else : 
            break
        

def delete_curso():
    print("")

def crear_curso(filename):
    while True:
        print("Ingrese el código")
        codigo = input(">>")
        if((validate_codigo_curso(codigo,cargar_datos(filename)))):
            break
        else:
            print("El codigo es unico") 
    while True:
        print("Ingrese el estado")
        estado = input(">>")
        if(estado != "DICTANDO"  and estado!="INACTIVO"):
            print("Debes ingresar un estado valido")
        else:
            break
    while True:
        print("Ingrese el nombre")
        nombre = input(">>")
        if(validate_nombre_curso(nombre,filename)):
            break
        else:
            print("Debes ingresar un nombre valido")
    while True:
        print("Ingrese los alumnos (xxxxx-xxxxx-xxxxx) donde xxxxxx son los códigos :")
        alumnos = input(">>")
        lista_alumnos =  alumnos.split("-")
        for a in lista_alumnos:
            if not alumno_existe(filename,a):
                print("Algún alumno no existe")
                continue            
        break
    while True:
        print("Ingrese los servidores (xxxxx-yyyyyyy-yyyyyyyy/xxxxx-yyyyyyy-yyyyyyyyyyyy) donde xxxxxx son los nombres y yyyyyy son los servicios permitidos :")
        servidores = input(">>")
        lista_servidores =  servidores.split("/")
        for l in lista_servidores:
            if not existe_servidor(filename,l.split("-")[0]):
                print("Algún Servidor no existe")
                continue
            for servicios in l.split("/")[1:]:
                if (not validar_servicios_Servidor(servicios,filename)):
                    print("Algún Servicio del servidor no existe")
                    continue
        break
    
    #CREAMOS EL CURSO
    alumnitos = []
    for i in alumnos:
        alumnitos.append(int(i))

    servidoresss= []
    for l in lista_servidores:
        servidor = l.split("-")[0]
        servs = l.split("/")[1:]

def validar_servicios_Servidor(servicios , filename):
    data = cargar_datos(filename)
    for i in data.get("servidores").get("servicios"):
        if(i.nombre!=servicios):
            return False
    return True

def validate_codigo_curso(codigo, data):
    cursos = data.get('cursos',[])
    for cu in cursos:
        if cu.codigo == codigo:
            return False
    return True
def validate_alumno_existe_codigo(code):
    for i in alumnos_global:
        if i.codigo ==  int(code):
            return True
    return False

def validate_nombre_curso(nombre, data):
    cursos = data.get('cursos',[])
    for cu in cursos:
        if cu.nombre == nombre:
            return False
    return True
def alumno_existe(filename , codigo):
    data =cargar_datos(filename)
    alumnos =  data.get('alumnos')
    for A in alumnos:
        if (str(A.codigo)) == codigo:
            return True
    return False
def existe_servidor(filename, nombre):
    data =cargar_datos(filename)
    servidores =  data.get('servidores')
    for A in servidores:
        if A.nombre == nombre:
            return True
    return False
def borrar_curso():
    print("")
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
                menu_crud_cursos(filename)
            else:
                print("Debe importar datos")
        elif opcion =="4" : 
            if(data!=""):
                menu_alumnos()
            else:
                print("Debe importar datos")
        elif opcion == "5":
                if data:
                    crud_servidores(data)
                else:
                    print("Debe importar datos primero.")
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
#CRUD ALUMNO-----------------------------------------------
#----------------------------------------------------------
def listar_alumnos():
    if len(alumnos_global) == 0:
        print('Los datos de los alumnos no han sido importados o no hay alumnos registrados.')
    else:
        print('\nLista de alumnos:')
        for alumno in alumnos_global:
            print('-'+alumno.nombre)

def listar_alumnos_filtros():
    if len(alumnos_global) == 0:
        print('Los datos de los alumnos no han sido importados o no hay alumnos registrados.')
    else:
        busqueda = input('Buscar alumnos por nombre: ')
        contador = 0
        for alumno in alumnos_global:
            if busqueda.lower() in alumno.nombre.lower():
                if contador == 0:
                    print('\nLista de alumnos:')
                print('-'+alumno.nombre)
                contador += 1
        if contador == 0:
            print('\nNo se encontraron alumnos con ese nombre.')

def mostrar_detalles_alumno():
    if len(alumnos_global) == 0:
        print('Los datos de los alumnos no han sido importados o no hay alumnos registrados.')
    else:
        codigo = input('Ingresa el código del alumno: ')
        for alumno in alumnos_global:
            if codigo == str(alumno.codigo):
                print('\nDetalles:')
                print(f'Nombre: {alumno.nombre}')
                print(f'Código: {alumno.codigo}')
                print(f'MAC: {alumno.mac}')
                return
        print('\nNo se encontró ningún alumno con ese código.')

def agregar_alumno(alumno):
        for al in alumnos_global:
            if al.codigo == alumno.codigo:
                if al.mac == alumno.mac:
                    print('Ya existe un alumno con este código y esta MAC.')
                else:
                    print('Ya existe un alumno con este código.')
            else:
                if al.mac == alumno.mac:
                    print('Ya existe un alumno con esta MAC.')
                else:
                    alumnos_global.append(alumno)
def registrar_alumno():
    nombre = input('Ingresa el nombre del alumno: ')
   
    while True:
        flag = True
        codigo = input('Ingresa el código del alumno: ')
        for alumno in alumnos_global:
            if str(alumno.codigo) == codigo:
                print('Ya existe un alumno con este código.')
                flag = False
                break
        if flag:
            break
   
    while True:
        flag = True
        mac = input('Ingresa la MAC de la VM del alumno: ')
        for alumno in alumnos_global:
            if alumno.mac == mac:
                print('Ya existe un alumno con esta MAC.')
                flag = False
                break
        if flag:
            break
   
    alumnos_global.append(Alumno(nombre,codigo,mac))
    print('|----------------------------------------|')
    print('|           Alumno registrado            |')
    print('|----------------------------------------|')
    print(f'Nombre: {nombre}')
    print(f'Código: {codigo}')
    print(f'MAC: {mac}')
def menu_alumnos():
    while True:
        print('\n|----------------------------------------|')
        print('|             MENU DE ALUMNOS            |')
        print('|         Seleccione una opción:         |')
        print('|----------------------------------------|\n')
        print('1) Listar todos los alumnos')
        print('2) Buscar alumno por nombre')
        print('3) Mostrar detalles de un alumno')
        print('4) Registrar un alumno')
        print('5) Salir\n')
        opcion = input('Elige una opción: ')
        if opcion == '1':
            listar_alumnos()
        elif opcion == '2':
            listar_alumnos_filtros()
        elif opcion == '3':
            mostrar_detalles_alumno()
        elif opcion == '4':
            registrar_alumno()
        elif opcion == '5':
            break
        else:
            print('Debes seleccionar una de las opciones del menú')
#CRUD ALUMNO-----------------------------------------------
#----------------------------------------------------------

#CRUD SERVIDORES--------------------------------------------
#----------------------------------------------------------
def listar_servidores(data):
    print("Servidores registrados:")
    for servidor in data.get("servidores", []):
        print(f"- Nombre: {servidor['nombre']}, IP: {servidor['ip']}")
def mostrar_detalle_servidor(data, nombre_servidor):
    servidores = data.get("servidores", [])
    servidor = next((s for s in servidores if s['nombre'] == nombre_servidor), None)
    if servidor:
        print(f"\nDetalles del servidor '{nombre_servidor}':")
        print(f"  - IP: {servidor['ip']}")
        print("  - Servicios:")
        for servicio in servidor.get("servicios", []):
            print(f"    - Nombre: {servicio['nombre']}")
            print(f"      Protocolo: {servicio['protocolo']}")
            print(f"      Puerto: {servicio['puerto']}")
    else:
        print(f"Servidor '{nombre_servidor}' no encontrado.")      
def crud_servidores(data):
    while True:
        imprimir_menu_crud()
        opcion = input("Seleccione una opción: ")
        if opcion == "2":
            listar_servidores(data)
        elif opcion == "3":
            nombre_servidor = input("Ingrese el nombre del servidor: ")
            mostrar_detalle_servidor(data, nombre_servidor)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
#CRUD SERVIDORES--------------------------------------------
#----------------------------------------------------------
if __name__ == "__main__":
    menu()
