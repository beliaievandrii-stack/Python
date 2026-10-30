def funktion1(name):
    print(f"Hallo, hier ist {name}")

funktion1("Andrii")

def funktion2(a):
    c = a + 10
    print(c)

funktion2(10)

def funktion3(a,b):
    sum = a+b
    print(sum)
    return sum

funktion3(100, 200)

def funktion4(parameter1, parameter2):
    sum = parameter1 + parameter2
    return sum

lösung = funktion4(100,200)
print(lösung)

def funktion5(parameter1, parameter2) :
    sum = (parameter1 + parameter2) / 2
    print("funktion 5: ", sum)
    return sum

funktion5(5,5)

def ups_das_klappt_nicht(a, b):
    c = a * b
    return c

ergebnis = ups_das_klappt_nicht(6,6)
print(ergebnis)

def funktion7():
    return 10

x = 100 + funktion7()
print(x)