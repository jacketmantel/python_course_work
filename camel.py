def main():
    name = input("camelCase: ")
    snake_case(name)
    

def snake_case(n):
    for c in n:
        if c.isupper():
            c = c.lower()  
            print("_", end="")  
        print(c, end="")
    
    print()

main()
