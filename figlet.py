from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    
    if len(sys.argv) == 3:
        if (sys.argv[1] == "--font" or sys.argv[1] == "-f"):
            if sys.argv[2] in fonts:
                user_input = input("Input: ")
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(user_input))
            else:
                sys.exit("Use another font. Invalid Font.")

    elif len(sys.argv) == 1:
        user_input = input("Input: ")
        rfonts = random.choice(fonts)
        figlet.setFont(font=rfonts)
        print(figlet.renderText(user_input))

    elif len(sys.argv) == 2:
        sys.exit("Not enough arguments")
    
    else:
        print("Stop spamming arguments")



main()