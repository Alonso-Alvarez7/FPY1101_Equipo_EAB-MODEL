# Menú base del programa
def datos_marco():
 print("Mi nombre es Marco Calfucura y tengo 18 años.")

def datos_gabriel():
    print("Mi nombre es Gabriel Diaz y tengo 27 años")

def datos_vicente():
   print("Mi nombre es Vicente Mitchell y tengo 22 años")


while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        datos_marco()
    elif op == "2":
        datos_gabriel()
    elif op == "3":
        datos_vicente()
    else:
        print(" Opción inválida.")
