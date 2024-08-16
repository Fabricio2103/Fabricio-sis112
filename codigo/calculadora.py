print("calculadora")

def calculadora():
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        try:
            x = input("seleccione una opcion:  ")

            if x in ['1', '2', '3', '4']:
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))

                if x == '1':
                    resultado = num1 + num2
                    print(f"{num1} + {num2} = {resultado}")

                elif x == '2':
                    resultado = num1 - num2
                    print(f"{num1} - {num2} = {resultado}")

                elif x == '3':
                    resultado = num1 * num2
                    print(f"{num1} * {num2} = {resultado}")

                elif x == '4':
                    if num2 == 0:
                        print("no se puede dividir por cero")
                    else:
                        resultado = num1 / num2
                        print(f"{num1} / {num2} = {resultado}")

            else:
                print("por favor escoge una de las siguientes opciones")

        except ValueError:
            print("error, por favor ingrese un numero valido")

if __name__ == "__main__":
    calculadora()
        


