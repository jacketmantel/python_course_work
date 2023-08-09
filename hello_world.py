

# Ask user their name, remove whitespace from str and Capitalize user's name
name = input("Whats your name? :3 ").strip().title()

# split users name into frist and last name
first, last = name.split(" ")


# say hello to user
print(f"hello, {first}")