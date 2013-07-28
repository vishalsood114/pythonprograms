import os
import sys

def main(dir):
    for i in os.listdir(dir):
        print i

main(sys.argv[1])
