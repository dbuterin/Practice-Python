x = raw_input("unesi prvi broj:")
x = int(x)
y = int(raw_input("unesi drugi broj:"))


operacija = raw_input("unesi matematicku operaciju :")

if operacija == "+":
    print "x+y=" + str(x + y)
elif operacija == "-":
    print "x - y = " + str(x - y)
elif operacija == "*":
    print "x * y = " + str(x * y)
elif operacija == "/":
    print "x / y = " + str(x / y)
else:
    print "Unesite ispravnu operaciju (+,-,*,/)"

print "Hvala"