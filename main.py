from juego import jugar_maquina, jugar_usuario


def main():
    print("Bienvenido al juego PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK")
    print("¿Contra quién quieres jugar? 1: Máquina | 2: Otro usuario")
    opcion = int(input("Introduce una opción 1 o 2: "))
    if opcion == 1:
        jugar_maquina()
    elif opcion == 2:
        jugar_usuario()
    else:
        print("Opción no válida. Inténtalo de nuevo.")
    
    jugar_de_nuevo = input("¿Quieres volver a jugar? (s/n): ").lower()
    if jugar_de_nuevo == "s":
        main


main()