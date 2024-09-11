import funciones_conversion

def conversiones():
    print("conversiones disponibles:")
    print("1. metros a kilometros")
    print("2. gramos a kilogramos")
    print("3. celsius a fahrenheit")
    print("4. Salir")

    while True:
        try:
            x = input("seleccione una opcion:  ")

            if x in ['1', '2', '3', '4']:
                # Se pide el numero que se desea realizar la conversion

                #Segun la opcion que se escogio se llama a la funcion correspondiente
                if x == '1':
                    a = int(input("Ingrese los metros: "))
                    print(f'longitud: {funciones_conversion.longitud(a)} km')
                
                if x == '2':
                    a = int(input("Ingrese los gramos: "))
                    print(f'masa: {funciones_conversion.masa(a)} kg')

                if x == '3':
                    a = int(input("Ingrese los grados celsius: "))
                    print(f'temperatura: {funciones_conversion.temperatura(a)} °F')
                    
                if x == '4':
                    break
            else:
                print("por favor escoge una de las siguientes opciones")
        
        except ValueError:
            print("error, por favor ingrese un numero valido")

if __name__ == "__main__":
    conversiones()
                    
