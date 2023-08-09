import random

def main():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        if n > 0:
            break
    
    level = random.randint(1, n)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        else:
            if guess < level:
                print("Too Small!\n")
                continue
            elif guess > level:
                print("Too high! Go lower. \n")
                continue
            else:
                print("Perfect answer! \n")
                break

main()