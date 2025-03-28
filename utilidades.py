import time
import random


VERDE = "\033[92m"
ROJO = "\033[91m"
AZUL = "\033[94m"
RESET = "\033[0m"


piedra = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
papel = """ 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
tijera = """ 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
lagarto = """ 
     _______
---'   ____)____
          ______)
       (________)
        (______)
---.__(____)
"""
spock = """ 
     _______
---'   ____)____
      (______ )
      (_______)
      (_______)
---.__(____)
"""


reglas = [
    {"opcion": 1, "nombre": "Piedra", "vence_a": [3, 4]},
    {"opcion": 2, "nombre": "Papel", "vence_a": [1, 5]},
    {"opcion": 3, "nombre": "Tijera", "vence_a": [2, 4]},
    {"opcion": 4, "nombre": "Lagarto", "vence_a": [2, 5]},
    {"opcion": 5, "nombre": "Spock", "vence_a": [1, 3]},
]

def mostrar_dibujo(opcion):
    dibujos = {1: piedra, 2: papel, 3: tijera, 4: lagarto, 5: spock}
    print(AZUL + dibujos.get(opcion, "Opción no válida") + RESET)


def determinar_ganador(usuario1, usuario2):
    if usuario1 == usuario2:
        return "empate"
    
    for regla in reglas:
        if regla["opcion"] == usuario1 and usuario2 in regla["vence_a"]:
            return "usuario1"
        elif regla["opcion"] == usuario2 and usuario1 in regla["vence_a"]:
            return "usuario2"
    
    return "empate"  # Por si acaso


def pensar():
    print("\nLa máquina está pensando", end="", flush=True)
    for _ in range(3):  
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")


