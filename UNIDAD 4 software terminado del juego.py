import random

opciones = ["piedra", "papel", "tijera"]

jugador = input("Elige piedra, papel o tijera: ").strip().lower()
pc = random.choice(opciones)

print("Tú elegiste:", jugador)
print("La PC eligió:", pc)

if jugador == pc:
    print("Empate")

# Opciones en las que el jugador gana
elif (jugador == "piedra" and pc == "tijera") \
     or (jugador == "papel" and pc == "piedra") \
     or (jugador == "tijera" and pc == "papel"):
    print("Ganaste")

# Opciones en las que el jugador pierde
elif (pc == "piedra" and jugador == "tijera") \
     or (pc == "papel" and jugador == "piedra") \
     or (pc == "tijera" and jugador == "papel"):
    print("Perdiste")

else:
    print("Opción no válida escribe piedra papel o tijera")

