#
#   Author - Rahul Ban
#

import hashlib
import random
import pandas as pd
import datetime as dt

def generate_password(password, num):
    pwd_list = []
    for i in range(1, num):
        pwd_gen = hashlib.sha256(str(password+str(i)).encode()).hexdigest()
        cut_pwd = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) + random.choice(list('.,!@#$%^&*()_+=-')) + pwd_gen[:8] + random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) + pwd_gen[9:14]
        pwd_list.append(cut_pwd)
        print("Secure Password ", i, " : ", cut_pwd)
    dict = {"Secure Passwords" : pwd_list}
    df = pd.DataFrame(dict)
    df.to_csv('Secure_passwords{}.csv'.format(dt.datetime.now().strftime("%Y-%m-%d %H%M%S"),index=False))
    print("Secure_passwords.csv : exported successfully !")

def generate_more(choice):
    if (choice == "y" or choice == "Y"):
        main()
    else:
        print("Exiting")
        exit()

def main():
    password = input('Enter your simple password: ')
    while True:
        try:
            num = int(input("Enter how many passwords to generate: "))
            generate_password(password, num+1)
            generate_more(input("Generate more passwords? (y) \n"))
            FALSE
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()