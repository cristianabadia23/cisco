def menu():
    try:
        print("1 Suma \n", "2 Resta \n", "3 muliplicacion \n", "4 division \n",
              "5 exponente \n", "6 Salir \n")
        selector = int(input("seleccion "))
        if selector == 1:
            sum(x=float(input("primer numero ")),
                y=float(input("segundo numero ")))
        if selector == 2:
            resta(
                x=float(input("primer numero ")),
                y=float(input("segundo numero ")))
        if selector == 3:
            multi(
                x=float(input("primer numero ")),
                y=float(input("segundo numero ")))
        if selector == 4:
            div(x=float(input("primer numero ")),
                y=float(input("segundo numero ")))
        if selector == 5:
            expo(
                x=float(input("primer numero ")),
                y=float(input("segundo numero ")))
        if selector == 6:
            salir()
    except ZeroDivisionError:
        print("Error!!!!!!\n", "No se puede dividir entre cero\n",
              "Vuelva a introducir los numeros\n")
        menu()
    except ValueError:
        print("Introduzca un numero")
        menu()


def sum(x, y):
    print("el resultado es ", x + y)
    salir()


def resta(x, y):
    print("el resultado es ", x - y)
    salir()


def multi(x, y):
    print("el resultado es ", x * y)
    salir()


def div(x, y):
    print("el resultado es", x / y)
    salir()


def expo(x, y):
    print("el resultado es ", x**y)
    salir()


def salir():
    selector2 = str(input("quieres volver S/N "))
    if selector2 == "S":
        menu()
    else:
        print("Hasta pronto")


print("Bienvenido a calculadora PY")
menu()
