def main():
    fname = input("File name: ").casefold().lower().lstrip()
    fcompare(fname)

def fcompare(filename):
    if filename.endswith(".jpg"):
        return print("image/jpg")
    elif filename.endswith(".jpeg"):
        return print("image/jpeg")
    elif filename.endswith(".gif"):
        return print("image/gif")
    elif filename.endswith(".png"):
        return print("image/png")
    elif filename.endswith(".pdf"):
        return print("application/pdf")
    elif filename.endswith(".txt"):
        return print("application/txt")
    elif filename.endswith(".zip"):
        return print("application/zip")
    else:
        print("application/octet-stream")

main()