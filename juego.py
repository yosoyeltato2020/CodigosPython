import random
from utilidades import mostrar_dibujo, determinar_ganador, reglas, VERDE, ROJO, RESET, pensar

cantidad_partidas = 3  

def jugar_maquina():
    puntuacion1 = 0
    puntuacion2 = 0

    while puntuacion1 + puntuacion2 < cantidad_partidas:
        print("\n1. Piedra\n2. Papel\n3. Tijera\n4. Lagarto\n5. Spock")
        usuario = int(input("Introduce una opción (1-5): "))
        
        opciones_validas = [regla["opcion"] for regla in reglas]
        if usuario not in opciones_validas:
            print(ROJO + "Opción no válida, intenta de nuevo." + RESET)
            continue

        pensar()
        maquina = random.choice(opciones_validas)

        print("\nTu elección:")
        mostrar_dibujo(usuario)
        print("\nElección de la máquina:")
        mostrar_dibujo(maquina)

        resultado = determinar_ganador(usuario, maquina)

        if resultado == "usuario1":
            puntuacion1 += 1
            print(VERDE + "¡Ganaste esta ronda!" + RESET)
        elif resultado == "usuario2":
            puntuacion2 += 1
            print(ROJO + "¡La máquina gana esta ronda!" + RESET)
        else:
            print("¡Empate!")

        print(f"Puntuación - Tú: {puntuacion1} | Máquina: {puntuacion2}")

    if puntuacion1 > puntuacion2:
        print(VERDE + f"\n¡Felicidades! Has ganado el mejor de {cantidad_partidas}." + RESET)
    else:
        print(ROJO + f"\n¡La máquina ganó el mejor de {cantidad_partidas}. ¡Suerte la próxima vez!" + RESET)

    














