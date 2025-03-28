from juego import jugar_maquina

def main():
    print("\nBienvenido a " + "\033[93m" + "Piedra, Papel, Tijera, Lagarto, Spock" + "\033[0m")
    print("¿Contra quién quieres jugar?")
    print("1. Contra la máquina")

    opcion = int(input("Introduce una opción (1): "))
    if opcion == 1:
        jugar_maquina()
    else:
        print("Opción no válida. Saliendo...")

if __name__ == "__main__":
    main()
