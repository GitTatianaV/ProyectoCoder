#Crear un programa en python que permita emular el registro y almacenamiento de usuarios en una base de datos. 
#la info esta guardada en una variable de tipo diccionario y las key seran nombre de usuario y los value seran las contraseñas
#Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.
#El formato de registro es: Nombre de usuario y Contraseña
#Utilizar una función para almacenar la información y otra función para mostrar la información
#Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor)
#Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario

#users = {
    #"Tatiana": "123",
    #"Lucas": "456",
    #"Florencia": "789"
#}

#def login(user, password):
 #if user in users and users[user] == password:
    #print("Inicio de sesion exitoso. ")
 #else: 
    #print("Usuario o contraseña inválida.")

#print("Bienvenido. Ingrese sus datos")
     
#username = input("Ingrese el nombre de usuario: ")
#pwd = input("Ingrese su contraseña: ")

#login(username, pwd)

users = {
    "Tatiana": "123",
    "Lucas": "456",
    "Florencia": "789"
}

def login(users, cantidad_intentos):
    intentos = 0
    while intentos < cantidad_intentos:
        print("Bienvenido. Ingrese sus datos")
        username = input("Ingrese el nombre de usuario: ")
        pwd = input("Ingrese su contraseña: ")

        if username in users and users[username] == pwd:
            print("Inicio de sesion exitoso. ")
            break
        else:
            print("Usuario o contraseña inválida.")
            intentos += 1
            print("Cantidad de intentos restantes: ", cantidad_intentos - intentos)
    else:
        print("Se alcanzó el máximo de intentos.")


cantidad_intentos = 3

login(users, cantidad_intentos)
  







