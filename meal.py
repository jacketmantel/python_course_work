def main():
    time = input("What time is it for you? ")
    convert(time)

def convert(time):
    hrs, mins = time.split(":")
    mins = float(mins) / 60 
    hrs = float(hrs)
    time = hrs + mins
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print("Not meal time")


if __name__ == "__main__":
    main()
