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
---'   ____)____
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

def mostrar_dibujo(opcion):
    if opcion == 1:
        print(piedra)
    elif opcion == 2:
        print(papel)
    elif opcion == 3:
        print(tijera)

def determinar_ganador(usuario1, usuario2):
    if usuario1 == usuario2:
        return "empate"
    elif (usuario1 == 1 and usuario2 == 3) or (usuario1 == 2 and usuario2 == 1) or (usuario1 == 3 and usuario2 == 2):
        return "usuario1"
    else:
        return "usuario2"

