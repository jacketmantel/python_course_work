def main():
    nov = input("Input: ")
    no_vowels_allowed(nov)

def no_vowels_allowed(word):
    vowels = ["a", "e", "i", "o", "u"]
    for i in word:
        if i.lower() in vowels:
            word = word.replace(i, "")
    print("Output: ", word)

main()