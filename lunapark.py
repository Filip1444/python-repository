godine = int(input("Unesite svoje godine: "))
visina = int(input("Unesite svoju visinu: "))

if godine < 16:
    if visina > 160 or visina <= 190:
        print("smijete se voziti")
    else:
        print("ne smijete se voziti ")
else:
    print("ne smijete se voziti")
