import os

def gettext(filename):
    return len(filename.split("."))

def main():
    files = os.listdir(".")
    print sorted(files,key=gettext)

if __name__ == "__main__":
    main()
