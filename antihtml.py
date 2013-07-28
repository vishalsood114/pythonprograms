import re
import sys

def main(filename):
    htmlfile = open(filename).read()
    return re.sub("<[^<>]*>","",htmlfile)

print main(sys.argv[1])
