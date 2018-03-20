#osoba
class Osoba(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        return self.first_name + " " +self.last_name
class Student(Osoba):
    def __init__(self, first_name, last_name, xica):
        self.first_name = first_name
        self.last_name = last_name
        self.xica = xica
    def setGrade(self, grade):
        self.grade = grade
    def hasPassed(self):
        return self.grade > 1

def main():
    osoba1 = Osoba("Ime", "Prezime")
    osoba2 = Osoba("Ime2", "Prezime2")
    print osoba1.first_name
    print osoba1.last_name
    print osoba2.full_name()

    osobe = [osoba1, osoba2]
    osobe.append(osoba1)
    for osoba in osobe:
        print osoba.full_name()

    student1 = Student("Student ime", "Student prezime", 43432432432)
    student1.setGrade(2)
    print student1.grade
    print student1.full_name()
    print student1.xica

if __name__ == '__main__':
    main()
