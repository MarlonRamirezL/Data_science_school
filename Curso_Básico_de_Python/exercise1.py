import datetime

now = datetime.datetime.now()

name = input("Hey, what's your name?\n")
age = int(input("Okay {}, how old are you?\n".format(name.title())))

yrs = (now.year +100) - age

msg = "Okay {}, so if you're {} now then you should turn 100 in the year {}".format(name.title(),age,yrs)

print(msg)

n = int(input("Okay {}, give me a number\n".format(name)))

print(msg * n)
print("Or does this look nicer?")
msg += "\n"
print(msg * n)


