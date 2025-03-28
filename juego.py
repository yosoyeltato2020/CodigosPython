import random
from utilidades import mostrar_dibujo, determinar_ganador

cantidad_partidas = 3

def jugar_maquina():
    puntuacion1 = 0
    puntuacion2 = 0

    while puntuacion1 + puntuacion2 < cantidad_partidas:
        print("\n1. Piedra\n2. Papel\n3. Tijera")
        usuario = int(input("Introduce una opción (1, 2 o 3): "))
        if usuario not in [1, 2, 3]:
            print("Opción no válida, intenta de nuevo.")
            continue

        maquina = random.choice([1, 2, 3])
        
        print("\nTu elección:")
        mostrar_dibujo(usuario)
        print("\nElección de la máquina:")
        mostrar_dibujo(maquina)
        
        resultado = determinar_ganador(usuario, maquina)
        
        if resultado == "usuario1":
            puntuacion1 += 1
            print("Ganaste esta ronda!")
        elif resultado == "usuario2":
            puntuacion2 += 1
            print("Gana la máquina!")
        else:
            print("Empate!")

        print(f"Puntuación - Tú: {puntuacion1} | Máquina: {puntuacion2}")

    if puntuacion1 > puntuacion2:
        print(f"\n¡Felicidades! Has ganado el mejor de {cantidad_partidas}.")
    else:
        print(f"\n¡La máquina ganó el mejor de {cantidad_partidas}. ¡Suerte la próxima vez!")

def jugar_usuario():
    puntuacion1 = 0
    puntuacion2 = 0

    while puntuacion1 + puntuacion2 < cantidad_partidas:
        print("\n1. Piedra\n2. Papel\n3. Tijera")
        
        usuario1 = int(input("Usuario 1, introduce una opción (1, 2 o 3): "))
        if usuario1 not in [1, 2, 3]:
            print("Opción no válida, intenta de nuevo.")
            continue
        
        usuario2 = int(input("Usuario 2, introduce una opción (1, 2 o 3): "))
        if usuario2 not in [1, 2, 3]:
            print("Opción no válida, intenta de nuevo.")
            continue

        print("\nUsuario 1 eligió:")
        mostrar_dibujo(usuario1)
        print("\nUsuario 2 eligió:")
        mostrar_dibujo(usuario2)
        
        resultado = determinar_ganador(usuario1, usuario2)
        
        if resultado == "usuario1":
            puntuacion1 += 1
            print("¡Usuario 1 gana esta ronda!")
        elif resultado == "usuario2":
            puntuacion2 += 1
            print("¡Usuario 2 gana esta ronda!")
        else:
            print("¡Empate!")

        print(f"Puntuación - Usuario 1: {puntuacion1} | Usuario 2: {puntuacion2}")

    if puntuacion1 > puntuacion2:
        print(f"\n¡Felicidades Usuario 1! Ganaste el mejor de {cantidad_partidas}.")
    else:
        print(f"\n¡Felicidades Usuario 2! Ganaste el mejor de {cantidad_partidas}.")







    














