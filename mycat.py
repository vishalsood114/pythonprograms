def mycat(filename):
    try:
        print open(filename).read()
    except IOError:
        print "No such file or directory %s exists" %filename

if __name__ == "__main__":
    import sys
    mycat(sys.argv[1])
