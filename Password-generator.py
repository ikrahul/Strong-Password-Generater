#
#   Author - Rahul Ban
#

import hashlib
import random


def generate_password(password, num):
    for i in range(1, num):
        pwd_gen = hashlib.sha256(str(password+str(i)).encode()).hexdigest()
        cut_pwd = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) + random.choice(list('.,!@#$%^&*()_+=-')) + pwd_gen[:8] + random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) + pwd_gen[9:14]
        print("Secure Password ", i, " : ", cut_pwd)

def generate_more(choice):
    if (choice == "y" or choice == "Y"):
        main()
    else:
        print("Exiting")
        exit

def main():
    password = input('Enter your simple password: ')
    num = int(input("Enter how many passwords to generate: "))
    generate_password(password, num+1)
    generate_more(input("Generate more passwords? (y) "))


if __name__ == '__main__':
    main()