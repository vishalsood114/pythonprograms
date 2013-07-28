import sys

lines = open(sys.argv[1]).readlines()

print "".join(lines[::-1])
