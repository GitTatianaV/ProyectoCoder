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