def main():
    cocaine()

def cocaine():
    due = 50
    while due > 0:
        print("Amount Due:", due)
        coin = int(input("Insert coin: "))
        if coin in [25, 10, 5]:
            due -= coin
    else:
        print("Change owed:", abs(due))
    
main()