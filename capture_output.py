from StringIO import StringIO
import sys

class capture_output:
    
    def __init__(self):
        self.buf = StringIO()

    def __enter__(self):
        self.oldstdout = sys.stdout
        sys.stdout = self.buf
        return self.buf

    def __exit__(self,*a):
        sys.stdout = self.oldstdout


with capture_output() as buf:
    print "one"
    print "two"

print "captured", repr(buf.getvalue())
