import math

# Constante de gravedad
GRAVEDAD = 9.81

# Menú de opciones
def mostrar_menu():
    print("\nBienvenido al solucionador de problemas de física.")
    print("Seleccione una opción:")
    print("1. Calcular fuerza neta (Segunda Ley de Newton)")
    print("2. Calcular fricción (estática o cinética)")
    print("3. Calcular peso de un objeto")
    print("4. Calcular fuerza normal en plano inclinado")
    print("5. Calcular aceleración usando la Segunda Ley de Newton (F = ma)")
    print("6. Calcular fuerza usando la Segunda Ley de Newton (F = ma)")
    print("7. Salir")

# Función para calcular la fuerza neta (Segunda Ley de Newton)
def calcular_fuerza_neta():
    masa = float(input("Ingrese la masa del objeto en kg: "))
    aceleracion = float(input("Ingrese la aceleración en m/s^2: "))
    fuerza_neta = masa * aceleracion
    print(f"La fuerza neta es: {fuerza_neta} N")

# Función para calcular la fricción (estática o cinética)
def calcular_friccion():
    tipo_friccion = input("¿Es fricción estática (e) o cinética (c)? ").lower()
    coeficiente = float(input("Ingrese el coeficiente de fricción: "))
    fuerza_normal = float(input("Ingrese la fuerza normal en N: "))
    if tipo_friccion == 'e':
        friccion_estatica = coeficiente * fuerza_normal
        print(f"La fuerza de fricción estática máxima es: {friccion_estatica} N")
    elif tipo_friccion == 'c':
        friccion_cinetica = coeficiente * fuerza_normal
        print(f"La fuerza de fricción cinética es: {friccion_cinetica} N")
    else:
        print("Tipo de fricción no reconocido. Use 'e' para estática o 'c' para cinética.")

# Función para calcular el peso de un objeto
def calcular_peso():
    masa = float(input("Ingrese la masa del objeto en kg: "))
    peso = masa * GRAVEDAD
    print(f"El peso del objeto es: {peso:.2f} N")

# Función para calcular la fuerza normal en un plano inclinado
def calcular_fuerza_normal():
    masa = float(input("Ingrese la masa del objeto en kg: "))
    angulo_inclinacion = float(input("Ingrese el ángulo de inclinación del plano en grados: "))
    fuerza_normal = masa * GRAVEDAD * math.cos(math.radians(angulo_inclinacion))
    print(f"La fuerza normal es: {fuerza_normal:.2f} N")

# Función para calcular la aceleración
def calcular_aceleracion():
    masa = float(input("Ingrese la masa del objeto (kg): "))
    fuerza = float(input("Ingrese la fuerza aplicada (N): "))
    aceleracion = fuerza / masa
    print(f"La aceleración del objeto es: {aceleracion:.2f} m/s²")

# Función para calcular la fuerza
def calcular_fuerza():
    masa = float(input("Ingrese la masa del objeto (kg): "))
    aceleracion = float(input("Ingrese la aceleración (m/s²): "))
    fuerza = masa * aceleracion
    print(f"La fuerza neta aplicada es: {fuerza:.2f} N")

# Programa principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ")
        
        if opcion == '1':
            calcular_fuerza_neta()
        elif opcion == '2':
            calcular_friccion()
        elif opcion == '3':
            calcular_peso()
        elif opcion == '4':
            calcular_fuerza_normal()
        elif opcion == '5':
            calcular_aceleracion()
        elif opcion == '6':
            calcular_fuerza()
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 7.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
