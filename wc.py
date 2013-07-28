import sys

def linecount(f):
    return len(open(f).readlines())

def wordcount(f):
    return len(open(f).read().split())

def charcount(f):
    return len(open(f).read())

def wc(files):
    linesum = 0
    wordsum = 0
    charsum = 0
    for f in files:
        linesum = linesum + linecount(f)
        wordsum = wordsum + wordcount(f)
        charsum = charsum + charcount(f)
        print "%7d %7d %7d %s" % (linecount(f),wordcount(f), charcount(f),f)

    print "%7d %7d %7d total" % (linesum,wordsum,charsum)

wc(sys.argv[1:])
