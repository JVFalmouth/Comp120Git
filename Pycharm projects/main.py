def idgen(nom):
    ide = ""
    for letter in nom:
        ide += str(ord(letter))
    return ide


name = input("Hello, what is your name? ")
age = int(input("How old are you? "))

print("Hello %s! On your next birthday you will be %i years old." % (name, age+1))

print("Your id is:", idgen(name))

zeroarray = [["0"for i in range(10)]for j in range(10)]

def print_array(array):
    displayString = ""
    for arr in array:
        for item in arr:
            displayString += item
        displayString += "\n"
    print(displayString)

print_array(zeroarray)