def convert(faces):
    print(faces.replace(":)", "🙂").replace(":(", "🙁"))
    return faces

def main():
    smile = input("What would you like to text? (Add :) or :( )    ")
    convert(smile)

main()



# done

'''
 implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂
 All other text should be returned unchanged.

 
'''