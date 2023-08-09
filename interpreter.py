def main():
    x, y, z = input(print("Expression: ")).split(" ")

    interpreter(x, y, z)

def interpreter(x, y, z):
    floatx = float(x)
    floatz = float(z)
    match y:
        case "+":
            print(round(floatx+floatz , 1))
        case "-":
            print(round(floatx-floatz, 1))
        case "*":
            print(round(floatx*floatz, 1))
        case "/":
            print(round(floatx/floatz, 1))





main()