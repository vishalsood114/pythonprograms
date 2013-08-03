def command(f):
    def g(filename):
        lines = read_lines(filename)
        lines = [f(line) for line in lines]
        print_lines(lines)

    return g

def read_lines(filenames):
    return (line for f in filenames for line in open(f))

def print_lines(lines):
    for line in lines:
        print line.strip("\n")

