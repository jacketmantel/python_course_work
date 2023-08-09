def main():
    g = input("Please Enter A Greeting: ").lower().replace(",", "")
    saidHello(g)

def saidHello(t):
    if t.split()[0] == "hello" and "hello" in t:
        print("$0")
    elif t.index("h") == 0:
        print("$20")
    else:
        print("$100")

main()
