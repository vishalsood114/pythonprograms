import sys

def print_freq(freq):
    items = sorted(freq.items(), key = lambda kv:kv[1], reverse = True)
    for k,v in items:
            print v,k

def read_words(filename):
    return open(filename).read().split()

def wordfreq(words):
    count = {}
    for w in words:
    #   if w not in words:
    #       freq[w] = 0
        count[w] = count.get(w,0) + 1
    return count

def main(filename):
    words = read_words(filename)
    freq = wordfreq(words)
    print_freq(freq)

main(sys.argv[1])
