saldo = 1000
operaciones = []
intentos = 0
clave = "1234"

# Rama: seguridad - validacion de clave

print("CAJERO AUTOMATICO")
clave_ingresada = input("Ingrese su clave: ")

while clave_ingresada != clave:
    intentos += 1
    if intentos >= 3:
        print("Demasiados intentos fallidos. Tarjeta bloqueada.")
        exit()
    print(f"Clave incorrecta. Intentos restantes: {3 - intentos}")
    clave_ingresada = input("Ingrese su clave: ")

print("Acceso concedido. Bienvenido!")

while True:
    print("MENÚ DEL CAJERO")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Su saldo actual es: ${saldo}")

    elif opcion == "2":
        deposito = float(input("Ingrese el monto a depositar: "))
        # Validacion rama
        if deposito <= 0:
            print("El monto debe ser mayor a 0.")
        elif deposito > 10000:
            print("No se puede depositar más de $10000 a la vez.")
        else:
            saldo += deposito
            operaciones += [f"Depósito: +${deposito}"]
            print("Depósito realizado con éxito.")

    elif opcion == "3":
        retiro = float(input("Ingrese el monto a retirar: "))
        # Validacion rama
        if retiro <= 0:
            print("El monto debe ser mayor a 0.")
        elif retiro > saldo:
            print("Fondos insuficientes.")
        elif retiro > 5000:
            print("No se puede retirar más de $5000 a la vez.")
        else:
            saldo -= retiro
            operaciones += [f"Retiro: -${retiro}"]
            print("Retiro realizado con éxito.")

    elif opcion == "4":
        print("\n--- HISTORIAL DE OPERACIONES ---")
        if len(operaciones) == 0:
            print("No hay operaciones registradas.")
        else:
            for op in operaciones:
                print(op)

    elif opcion == "5":
        print("Gracias por usar el cajero automático.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")