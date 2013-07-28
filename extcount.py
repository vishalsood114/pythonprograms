import sys
import os

def print_count(count):
    items = sorted(count.items(),key=lambda kv:kv[1],reverse = True)
    for k,v in items:
        print v,k

def main(dir):
    count = {}
    for i in os.listdir(dir):
        i = i.split('.')[1]
        count[i] = count.get(i,0) + 1
    
    print_count(count)

main(sys.argv[1])
