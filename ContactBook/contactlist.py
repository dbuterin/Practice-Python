class ContactList(object):
    def __init__(self):
        self.list = []
    def add(self, contact):
        self.list.append(contact)
    def delete(self, index):
        del self.list[index]
    def show(self):
        for i in range(0, len(self.list)):
            print str(i + 1) + " " + self.list[i].fullName()
    def getIndex(self):
        contact_index = raw_input("Unesi redni broj osobe: ")
        contact_index = int(contact_index) - 1
        if contact_index < len(self.list):
            return contact_index
        else:
            print "Unesite broj manji od " + str(len(contacts) + 1)
            return -1