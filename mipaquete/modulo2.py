#Crear un programa que permita el modelamiento de Clientes en una página de compras 

#crear un paquete redistribuible con el programa creado.

#El proyecto debe ser un archivo comprimido del paquete. Formatos aceptados: .zip o .tar.gz bajo el nombre “Segunda pre-entrega+Apellido”.

#Para crear el paquete distribuible también como adicional el archivo de la Pre entrega #1.

#La Clase Cliente debe tener mínimo 4 atributos y 2 métodos.

class Cliente():
    def __init__(self, nombre, apellido, direccion, razonsocial, email):
     self.nombre = nombre
     self.apellido = apellido
     self.direccion = direccion
     self.razonsocial = razonsocial
     self.email = email

#Se debe utilizar el método __str__() para darle nombre a los objetos.
    def __str__(self):
     return f"Hola cliente: {self.nombre} {self.apellido}"
    
#Metodo comprar  
    def comprar(self, producto, cantidad):
     print(f"{self.nombre} ha comprado {cantidad} {producto}")

#Metodo ver informacion del cliente
    def ver_informacion_cliente(self):
        print(f"Información del cliente {self.nombre} {self.apellido}:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Dirección: {self.direccion}")
        print(f"Razón Social: {self.razonsocial}")
        print(f"Email: {self.email}")
    
  
Cliente1 = Cliente("Tatiana", "Velehorski", "Arismendi", "LaTribuSRL", "tati.velehorski@gmail.com")
print(Cliente1)

Cliente2 = Cliente("Lucas", "Villamayor", "Losincas", "CapielloSRL", "Lucas.villamayor@gmail.com")
print(Cliente2)
Cliente1.comprar("Notebooks", 2)
Cliente2.comprar("Celular", 1)

Cliente1.ver_informacion_cliente()
Cliente2.ver_informacion_cliente()




