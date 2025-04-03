class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b

def main():
    print("Calculadora - Operaciones: suma, resta, multiplicacion, division")
    try:
        a = int(input("Introduce el primer número (0-10): "))
        b = int(input("Introduce el segundo número (0-10): "))
        
        if not (0 <= a <= 10 and 0 <= b <= 10):
            print("Los números deben estar entre 0 y 10")
            return

        operacion = input("Elige la operación (suma, resta, multiplicacion, division): ").strip().lower()
        calc = Calculadora()

        if operacion == "suma":
            resultado = calc.suma(a, b)
        elif operacion == "resta":
            resultado = calc.resta(a, b)
        elif operacion == "multiplicacion":
            resultado = calc.multiplicacion(a, b)
        elif operacion == "division":
            resultado = calc.division(a, b)
        else:
            print("Operación no válida")
            return

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Por favor, ingresa números válidos")
    except ZeroDivisionError as e:
        print(e)

if __name__ == '__main__':
    main()
