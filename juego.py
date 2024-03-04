import random
import sys

usuario = len(sys.argv[1])

opciones = ["piedra", "papel", "tijeras"]
npc = random.choice(opciones)

print(f"jugaste {usuario}")
print(f"juega la computadora {npc}")


if usuario in opciones:
    if usuario == npc:
        print("empate")
    
    elif ((usuario == "piedra" and npc == "tijera") or
          (usuario == "papel" and npc == "piedra") or
          (usuario == "tijera" and npc == "papel")):
        print("ganaste")
    
    else:
        print("perdiste")
    
else:
    print(f"las opciones solo son piedra, papel o tijera")
    

