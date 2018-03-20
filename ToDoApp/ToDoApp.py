print "TODO aplikacija"
taskovi = {}




while True:
    task = raw_input("Unesite task: ")
    done = raw_input("Rijeseno (y/n): ").lower()
    taskovi[task] = (done == "y")
    print "Vas task %s" % task
    jos = raw_input("Zelite li jos (y/n): ")
    if jos.lower() != "y":
        break
print "Rijeseni taskovi"
for task in taskovi:
    if taskovi[task]:
        print task

print "Ne rijeseni taskovi"
for task in taskovi:
    if not taskovi[task]:
        print task

file = open("taskovi.txt", "w+")
for task in taskovi:
    file.write(task + ";" + str(taskovi[task]) + "\n")
file.close()
print "Kraj"
