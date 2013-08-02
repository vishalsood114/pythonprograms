import os
#import grep
import sys

##def count_lines(f):
##    return len(open(f).readlines())

def read_files (filenames):
    return (line for f in filenames for line in open(f))
#    for f in filenames: 
#        for line in open(f):
#            yield line

def count_iter(seq):
    
    return sum(1 for x in seq)
#    count = 0
#    for x in seq:
#        count += 1
#    return count

def main():
    filenames = sys.argv[1:]
    lines = read_files(filenames)       
    linecount = count_iter (lines)
    print linecount

if __name__ == "__main__":
    main()
