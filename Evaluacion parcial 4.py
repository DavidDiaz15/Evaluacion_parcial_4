compra = {
}

func1 = 150
func2 = 180
ventas1 = 0
ventas2 = 0

def menu():
    print("TOTEM AUTOATENCIÓN CAFECONLECHE")
    print("1.- Comprar entrada Cats")
    print("2.- Cambio de funcion")
    print("3.- Mostrar stock")
    print("4.- Salir")

def comprar_entrada():
    global func2, func1, ventas1, ventas2
    if func1 >= 1 and func2 >= 1:
        while True:
            nombre = input("Nombre del comprador: ")

            if nombre.isalpha() and len(nombre) > 3:
                break

            else:
                print("Ingrese un nombre válido.")

        if nombre in compra:
            print("Su nombre ya se encuentra registrado.")
        
        else:
            print("Nombre registrado con éxito.") 
            print("-" * 30)
            print("Funciones disponibles")
            print(f"Función 1: Cats Dia Viernes. {func1} entradas disponibles")
            print(f"Función 2: Cats Dia Sabado. {func2} entradas disponibles")
            print("-" * 30)

            while True:
                while True:
                    try:
                        funcion = int(input("Qué función deséa agendar? (1 / 2): "))
                        break
                    
                    except ValueError:
                        print("Ingrese un número entero positivo.")

                if funcion == 1:
                    compra[nombre] = {'funcion': funcion}
                    func1 = func1 - 1
                    ventas1 = ventas1 + 1
                    print("Entrada registrada en la función 1. Stock restante:")
                    print(f"{func1} Día viernes.")
                    print(f"{func2} Día sabado.")
                    print("-" * 30)
                    break
                
                elif funcion == 2:
                    compra[nombre] = {'funcion': funcion}
                    func2 = func2 - 1
                    ventas2 = ventas2 + 1
                    print("Entrada registrada en la función 2. Stock restante:")
                    print(f"{func1} Día viernes.")
                    print(f"{func2} Día sabado.")
                    print("-" * 30)
                    break
                else:
                    print("Ingrese una función válida!")

def cambio():
    global func1, func2, ventas1, ventas2, compra

    if not compra:
        print("No hay compras realizadas.")
            
    else:
        buscar = input("Ingrese nombre del comprador para cambiar de funcion: ")

        if buscar in compra:

            datos = compra[buscar]

            print("Reserva encontrada")
            

            if datos['funcion'] == 1:
                        
                cambio_func = input("Desea cambiar su funcion a la del dia sabado? (s/n): ")
            
                if cambio_func == "s":
                    compra[buscar] = {'funcion': 2}
                    print("Reserva cambiada a dia sabado")
                    func2 = func2 - 1
                    func1 = func1 + 1
                    ventas1 = ventas1 - 1
                    ventas2 = ventas2 + 1   
            
                elif cambio_func == "n":
                    print("No se realizara ningun cambio.")
                        
            
                else:
                    print("Ingrese opcion valida")

        
            elif datos['funcion'] == 2:
                        
                cambio_func = input("Desea cambiar su funcion a la del dia viernes? (s/n): ")
                        
                if cambio_func == "s":
                    compra[buscar] = {'funcion': 1}
                    func1 = func1 - 1
                    func2 = func2 + 1
                    ventas1 = ventas1 + 1
                    ventas2 = ventas2 -1
                        
                            
                elif cambio_func == "n":
                    print("No se realizara ningun cambio.")
                        
            
                else:
                    print("Ingrese opcion valida")
        else:
            print("Nombre no se encuentra registrado.")

def mostrar_stock():
    global func1, func2, ventas1, ventas2
    print("-- STOCK DE FUNCIONES --")
    print(F"Función 1 (Viernes): {func1} disponibles.")
    print(F"Función 2 (Sabado): {func2} disponibles.")
    print("")
    print("-- STOCK DE VENTAS --")
    print(F"Función 1 (Viernes): {ventas1} vendidas.")
    print(F"Función 2 (Sabado): {ventas2} vendidas.")

def cuerpo():
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
        except ValueError:
            print("Ingrese una opción válida.")
            continue

        if opc == 1:
            comprar_entrada()
            break
        elif opc == 2:
            cambio()
            break
        elif opc == 3:
            mostrar_stock()
            break
        elif opc == 4:
            print("Programa terminado...")
            exit()
        else:
            print("Ingrese una opción válida.")

def main():
    while True:
        menu()
        cuerpo()

main()
