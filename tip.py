def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO DONE
     float_dollar = float(d.removeprefix('$'))
     return float_dollar


def percent_to_float(p):
    # TODO DONE
    float_percent = float(p.removesuffix('%')) / 100
    return float_percent


main()



#done