import random
import string
import time

passwords = open("Paswords.txt", "a")
cont = "y"
tot = 0

list_s = ['!', '?', '$', '%', '^', '&', '*', '(', ')', '_', '+', '/']
list_n = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list_l = []

def get_choices(y):
    for j in range(x):
        list_c.append(random.choice(y))
    
def letters(p):
    for letter in p:
        list_l.append(letter)

print("\t\tWelcome to Random Password Generator")
while cont == "y":
    password = ""
    
    list_c = []
    
    letters(string.ascii_uppercase)
    letters(string.ascii_lowercase)

    random.shuffle(list_l)

    print("\t\t", "-" * 33)

    list_list = [list_n, list_l, list_s]
    typ = ["numbers", "letters", "special characters"]

    while cont == "y":
        
        for i in range(3):
            while True:
                try:
                    x = int(input("How many "+typ[i]+" add to your password? "))
                except ValueError:
                    print("Integer Required")
                    continue
                break
            tot += x
            get_choices(list_list[i])
        print()    
        
        while True:
            cont = input("Do you want to add more characters, enter 'y' or enough enter 'q': ").lower()
            if cont != "y" and cont != "q":
                print("Invalid Command !")
                continue
            break
    
    random.shuffle(list_c)

    for i in range(tot):
        password += random.choice(list_c)
    print()
    print("Generating Please Wait ! ")
    for i in range(25): #Fake Loading Bar
        print("|", end="")
        time.sleep(0.01)
    print(" 100%")
    print()    
    print("Your password is successfully generated ! -", "*" * tot)
    print()

    visible = input("Enter \"y\" to make it visible : ").lower()
    print()
    
    print("-" * 63)
    print("Your password is :", password)
    print("-" * 63)
    save = input("Enter 's' to save password in text file: ")
    if save == "s":
        name = input("Give a name to this password: ")
        passwords.write("\n"+name+" : "+password)
        
    while True:
            cont = input("Enter 'y' to generate another password or 'q' to quit: ").lower()
            if cont != "y" and cont != "q":
                print("Invalid Command !")
                continue
            break
    
    print()
else:
    passwords.close()
    print("Thank you for using !")
