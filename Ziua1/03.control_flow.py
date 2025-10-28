

x = 20

if x > 30:
    print("x este mai mare decat 30")
else:
    print("x nu este mai mare ca 30")



varsta = 22

if varsta < 18:
    print("Minor")
else:
    if varsta < 30:
        print("Young adult")
    else:
        if varsta < 65:
            print("Adult")
        else:
            print("Pensionar")

 

if varsta < 18:
    print("Minor")
elif varsta < 30:
    print("Young adult")
elif varsta < 65:
    print("Adult")
else:
    print("Pensionar")