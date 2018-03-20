from contact import Contact
from contactlist import ContactList

def main():
    print "Imenik"
    contacts = ContactList()
    while True:
        print "-----------"
        print "-----------"
        print "1 za unos novih korisnika"
        print "2 za ispis svih korisnika"
        print "3 za edit korisnika"
        print "4 za brisanje korisnika"
        odabir = raw_input("Unesi broj: ")
        print "-----------"
        print "-----------"
        if odabir == "1":
            contact = Contact()
            contact.setData()
            contacts.add(contact)
        elif odabir == "2":
            contacts.show()
        elif odabir == "3":
            contacts.show()
            index = contacts.getIndex()
            if index > -1:
                contacts.list[index].setData()
        elif odabir == "4":
            contacts.show()
            index = contacts.getIndex()
            if index > -1:
                contacts.delete(index)
if __name__ == '__main__':
    main()