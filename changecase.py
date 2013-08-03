from command0 import command
import sys

@command
def uppercase(line):
    return line.upper()

@command
def lowercase(line):
    return line.lower()

if __name__ == "__main__":
    uppercase(sys.argv[1:])
    lowercase(sys.argv[1:])

