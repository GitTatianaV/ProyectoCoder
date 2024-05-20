#def suma_diez_mas_cinco():
#print("haciendo algunas cosas...")
#def suma_diez_mas_cinco():

#print("mi aplicacion hacinedo mas cosas...")
#def suma_diez_mas_cinco():

#si quiero modificar o mejorar algo en el codigo de mi pag web. La mantencion del cod se hace compleja ir cod por cod porque en la realidad hay millones de lineas de cod
#lo ideal es tener un lugar donde tengamos almacenada la logica/procedimiento

#print(len("Mauricio"))
#print(8)
#como le digo a una funcion que se resuelva a un determinado valor?

#print(par_o_impar(5)) se resuelve a None porque dentro de la invocacion tenemos que retornar algo, decirle a qué se resuelve. Esto se lo digo con la palabra return

#def par_o_impar(num):

    #if num % 2 == 0:
     #return "Es par"
    #else:
       #return "Es impar"
    
#print(par_o_impar(5))

#como una funcion se podria adaptar a diferentes escenarios? que sea mas flexible

#def calcula(op, a, b):
    #if op == "sum":
        #return a + b
        #print(f"la suma de {a} + {b} es {a + b}")
    #elif op == "res":
        #print(f"la resta de {a} - {b} es {a - b}")
    #elif op == "mul":
        #print(f"la mul de {a} * {b} es {a * b}")
    #else:
        #print("operacion no valida")
#print("haciendo cosas")
#resultado = 20 + calcula("sum", 10, 5)
#print(resultado)

#calcula("sum", 10, 5)
#calcula("res", 9, 4)
#calcula("mul", 10, 6)
#print("haciendo mas cosas")

#nombre = "Ariel" variable global

#def saluda():
 
    #return f"Hola {nombre}"

#print(saluda())
#print(nombre)


#def devuelve_impares():
 #return 20, 30, 40 --> py infiere que es una tupla, si no le pongo parentesis py infiere que es tupla
 #return (20, 30, 40)

#print(devuelve_impares())

class Cliente:
    def _init_(self, nombre, apellido, edad, direccion, telefono, email, interes):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.interes = interes
        self.puntos = 0

    def comprar(self, producto, tienda):
        print(f"{self.nombre} ha comprado {producto} en {tienda}.")
        self.sumar_puntos(10)  # Añadir puntos por la compra

    def sumar_puntos(self, cantidad):
        self.puntos += cantidad

    def imprimir_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Email: {self.email}")
        print(f"Intereses: {self.interes}")
        print(f"Puntos acumulados: {self.puntos}")  # Mostrar los puntos acumulados

    def _str_(self):
        return f"Hola, soy el cliente {self.nombre} {self.apellido}, tengo {self.edad} años, mis datos son los siguientes:\nDirección: {self.direccion}\nTeléfono: {self.telefono}\nEmail: {self.email}\nPuntos acumulados: {self.puntos}"

