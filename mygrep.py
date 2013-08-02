import sys

def grep (pattern,lines):
    for line in lines:
        #print "grep",repr(line)
        if pattern in line:
            yield line

def uppercase (seq):
    for x in seq:
        #print "uppercase", repr(x)
        yield x.upper()

def print_lines(lines):
    for line in lines:
        #print "print_line", repr(line)
        print line.strip("\n")

def main():
    pattern = sys.argv[1]
    filename = sys.argv[2]
    f = open(filename)
    lines = grep(pattern,f)
    print_lines(lines)

if __name__ == "__main__":
    main()
