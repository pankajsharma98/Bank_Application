""" this is a simple bank application having some baisc
functionalities such as 
    debit
    credit
    check balance
    update password
"""


import os
import time
import random
import shelve
from getpass import getpass
#from log import update_log
#from auth import login,signup



def main_menu():
   # update_log("INFO","Application Started")
    os.system('cls')
    print("\n\n")
    print(f"\n\n\t {time.ctime()} welcome user")
    s="""
        \t\t1.Login
        \t\t2.SignUp
        \t\t3.Exit
    """
    print(s)
    while True:
        try:
            print("\n")

            ch=int(input("\t\tenter your choice:".rjust(30)))
            if ch < 1 or ch > 3:
                print("\n\n\t\tError!!! Invalid choice")
                continue
            break
        except ValueError as e:
            print("\n\n\t\tError!!! Press only integer number")

    if ch==1:
    #    update_log("INFO","User tried to login")
        login()
        main_menu()
    elif ch==2:
    #    update_log("INFO","User tried to signup")
        signup()
        main_menu()
    elif ch==3:
       # main_menu()
        os.system('cls')
        print("\n\n")
        print("\t\t thank for using our services")
        print("\n\n\t\t...........Exiting............")
       # update_log("INFO","Application closed")
        time.sleep(random.randint(2,5))
        os.system('cls')




#if __name__=="__main__":
    
    
    
"""
    we auth functions like login and signup
"""

#import os
#import time
#import shelve
#import getpass
#from trans import sub_menu
#from log import update_log


def login():
    acc=input("\n\n\t\t Enter your account number:")
    db=shelve.open("database/users_data")
    if acc in db.keys():
        password = getpass("\n\t\tPassword:")
        if password == db[acc]['password']:
    #        update_log("Login",f"login sucessfully for acc no {acc}")
            sub_menu(acc)
        else:
     #       update_log("Error",f"login unsucessfully for acc no {acc} because of password Verification")
            print("\n\n\t\tinvalid password....Try Again")
    else:
      #  update_log("DENY","unauthoriged account accessed")
        print("\n\n\t\tError!!! invalid account number")
        print("\n\n\t\tif ypu are a new user please signup first")

    print("\n\n\t\t..........redirecting to main menu..........")
    time.sleep(2)


def signup():
    os.system('cls')
    print("\n\n\t\tWelcome to signup service\n\n")
    print(f"\n\n\t\ttime:{time.ctime()}")
    name=input("\n\n\t\tEnter your name:")
    balance=eval(input("\n\t\tEnter your initial amount:"))
    password=getpass("\n\t\tPassword:")
    db=shelve.open("database/users_data",writeback=True)
    acc_no=db.get('last_acc')+1
    db['last_acc']=acc_no
    acc_no=str(acc_no)
    db[acc_no]={'name':name,'balance':balance,'password':password}
    db.close()
   # update_log("SignUp",f"signup sucessfully for acc no {acc_no} because of password varification")
    print("\n\n\t\tAccount create sucessfully write down your account number")
    print(f"\n\n\t\tyour account number is {acc_no} and used to login \n\n")
    input("\n\n\t\t..........Press any key to continue..........")

    
    
#from bank_application import main_menu
#from auth import login,signup
#import shelve
#import time
#import os
#import getpass
#from log import update_log

def sub_menu(acc_no):
    s="""\t\t1.Credit \n\t\t2.debit \n\t\t3.check balance \n\t\t4.update password \n\t\t5.logout"""
    print(s)
    while True:
        try:
            print("\n")
            ch=int(input("\t\tEnter your choice:".rjust(30)))
            if ch<1 or ch>5:
                print("\n\n\t\tError!!! Invalid choice")
                continue
            break
        except ValueError as e:
            print("\n\n\t\tError!!! press only integer number...")


    if ch ==1:
    #    update_log("INFO","user credit some money")
        credit(acc_no)
    
    elif ch ==2:
     #   update_log("INFO","user debit some money")
        debit(acc_no)

    elif ch ==3:
      #  update_log("INFO","user check acconut balance")
        check_balance(acc_no)

    elif ch ==4:
       # update_log("INFO","user set new password")
        update_password(acc_no)

    elif ch==5:
        #update_log("INFO","go to logout")
        logout()

    print("\t\tyou are at menu of logged in function")




def credit(acc_no):
    amount=int(input("\t\tenter amount to be cerdit:"))
    db=shelve.open("database/users_data",writeback=True)
    new_balance=db[acc_no]['balance']+amount
    db[acc_no]['balance']=new_balance
    db.close()
    #update_log("CREDIT",f"user acc no {acc_no} credit some money")
    print(f"\t\tyour update balance is {new_balance}")
    sub_menu(acc_no)


def debit(acc_no):
    amount=int(input("\t\tEnter amount to be debit:"))
    db=shelve.open("database/users_data",writeback=True)
    new_balance=db[acc_no]['balance']-amount
    db[acc_no]['balance']=new_balance
    db.close()
    #update_log("DEBIT",f"user acc no {acc_no} debit some money")
    print(f"\t\tyour update balance is {new_balance}")
    sub_menu(acc_no)

def check_balance(acc_no):
    db=shelve.open("database/users_data",writeback=True)
    current_balance=db[acc_no]['balance']
    db[acc_no]['balance']=current_balance
    db.close()
    #update_log("CHECK_BALANCE",f"user acc no {acc_no} check account balance")
    print(f"\t\tyour update balance is {current_balance}")
    sub_menu(acc_no)


def update_password(acc_no):
    p1=getpass("\t\tEnter password:")
    p2=getpass("\t\tVerify password:")
    if p1==p2:
        db=shelve.open("database/users_data",writeback=True)
        db[acc_no]['password']=p1
     #   update_log("UPDATE_BALANCE",f"user acc no{acc_no} changed account password")
        print("\n\n\t\tpassword sucessfully updated")
        print("\n\n\t\tplease login again to verify")
        sub_menu(acc_no)
    else:
        print("\n\n\t\tpassword does not match")
        print("\n\t\ttry again!!!")
        update_password(acc_no)

def logout():
	print("\n\n\t\tThanks for using services.")
	time.sleep(4)
	os.system("cls")
main_menu()
