import sys

srccont = open(sys.argv[1]).read()

destfile = open(sys.argv[2],"w")

destfile.write(srccont)

destfile.close()
