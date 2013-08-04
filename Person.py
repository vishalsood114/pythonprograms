class Person(object):
    def __init__(self, firtname,lastname, phone):
        self.firstname = firstname
        self.lastname = lastname
        self._phone = phone

    @property
    def phone(self):
        return self._phone
    
    @fullname.setter
    def fullname(self, firstname, lastname):
        self._fullname = firstname + " " + lastname
        
    @property 
    def fullname(self):
        return self.firstname + " " + self.lastname

    @phone.setter
    def phone(self, value):
        if len(value) == 10:
            self.value = value
        else:
            raise ValueError("Invalid phone number %r" % value)

    def __repr__(self):
        return "Person(%r, %r)" % (self.fullname, self.phone)
    
