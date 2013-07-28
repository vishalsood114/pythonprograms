import sys

def parse_csv(f):
    lines = open(f).readlines()
    return [ x.strip("\n").split(',') for x in lines   ]
    
print parse_csv(sys.argv[1])
