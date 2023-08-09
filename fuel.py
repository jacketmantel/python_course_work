def main():
    while True:
        try:
            result = fraction("Fraction: ")
            gauge = min_max(result)
        except (ValueError, ZeroDivisionError, NameError):
            pass
        else:
            print(gauge)
            break


def fraction(prompt):
    fract = input(prompt).split("/")
    return abs(round(int(fract[0]) / int(fract[1]) * 100))


def min_max(number):
    if 99 <= number <= 100:
        return "F"
    if number <= 1:
        return "E"
    if number > 100:
        return main()
    else:
        return f"{number}%"


main()
