import emoji


def main():
    user_emoji = input("Input: ")
    user_emoji = emoji.emojize(user_emoji, language="alias")
    print("Output: ", user_emoji)


main()
