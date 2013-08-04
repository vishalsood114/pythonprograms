"""
Folder class to give a dictionary like interface to a folder on a disk
"""
import os

class Folder:
    def __init__(self,f):
        self.f = f

    def __getitem__(self,filename):
        path = os.path.join(self.f,filename)
        return open(path).read()

    def __setitem__(self,filename,value):
        path = os.path.join(self.f,filename)
        open(path,'w').write(value)
    
    def __len__(self):
        return  len(os.listdir(self.f))

    def __contains__(self,filename):
        path = os.path.join(self.f,filename)
        return os.path.exists(path)

#created a test folder in the current directory where you are running the python program
t = Folder("test")
print "Length: \n", len(t)
print "__getitem__:\n", t['a.txt']
print "__contains__:"
print 'b.txt' in t
print 'c.txt' in t
print "__setitem__:"
t['c.txt'] = 'hello, world'
