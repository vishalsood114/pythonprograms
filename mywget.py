import urllib
import sys

def main(path):
    data = urllib.urlopen(path).read()
    if path[-1] == '/':
        fileindex = open("index.html",'w')
        fileindex.write(data)
        fileindex.close()
        print "saving %s as index.html" %path
    else:
        filename = path.split("/")[-1]
        fileinterp = open(filename, 'w')
        fileinterp.write(data)
        fileinterp.close()
        print "saving %s as %s" %(path,filename)

main(sys.argv[1])
