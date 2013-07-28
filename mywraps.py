import sys

def wordboundry():
    pass

def splitline(line,w):
    if not line:
        return [""]

    parts = []
    for i in range(0,len(line),w):
        parts.append(line[i:i+w])
    return parts

def mywrap(filename, width):
    lines = open(filename).readlines()
    for line in lines:
        for part in splitline(line.strip("\n"),width):
            print part


if __name__ == "__main__":
    mywrap(sys.argv[1],int(sys.argv[2]))

