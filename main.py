respuesta = "s"
puntaje_jugador = 0
puntaje_maquina = 0
while respuesta == "s":
    from random import *
    print("*********Bienvenidos al juego de piedra, papel y tijera:*********")
    jugador = input("Ingrese su jugada: ")
    eleccion = ["piedra", "papel", "tijera"]
    computadora = eleccion[randint(0,2)]
    print("La jugada de la computadora es: ", computadora)
    if computadora == jugador:
        print("Es un empate.")
    elif computadora == "piedra" and jugador == "tijera":
        print("La computadora ganó.")
        puntaje_maquina += 1
    elif computadora == "papel" and jugador == "tijera":
        print("Tú ganaste.")
        puntaje_jugador += 1
    elif computadora == "tijera" and jugador == "piedra":
        print("Tú ganaste.")
        puntaje_jugador += 1
    elif computadora == "papel" and jugador == "piedra":
        print("La computadora ganó.")
        puntaje_maquina += 1
    elif computadora == "piedra" and jugador == "papel":
        print("Tú ganaste.")
        puntaje_jugador += 1
    elif computadora == "tijera" and jugador == "papel":
        print("La computadora ganó.")
        puntaje_maquina += 1
    print("Tu puntaje es: ", puntaje_jugador)
    print("El puntaje de la máquina es: ", puntaje_maquina)
    print("Desea continuar Si(s) o No(n)")

    respuesta = input()

