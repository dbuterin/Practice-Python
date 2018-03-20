#za funkciju radoma pyton je ima definiranu
import random

#definicija podataka
data = {"Hrvatska":"Zagreb",
        "Slovenija":"Ljubljana",
        "Srbija":"Beograd"
        }
def randdrzava():
    current = random.randint(0, len(data) - 1)
    keys = data.keys()
    return keys[current]

def quiz():
    drzava = randdrzava()
    grad= raw_input("Koji je glavni grad " + drzava + ":")
    return data[drzava].lower() == grad.lower()
    #if grad.lower() == True:
     #   return
      #  return False

def main():
    while True:
        res =  quiz()
        if res:
            print "Bravo sve znas"
        else:
            print "Krivo"
        if "y" != raw_input("HOCES JOS?"):
            break


if __name__ == '__main__':
    main()