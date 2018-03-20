class Contact(object):
    def setData(self):
        self.first_name = raw_input("Unesi ime: ")
        self.last_name = raw_input("Unesi prezime: ")
    def fullName(self):
        return self.first_name + " " +self.last_name
