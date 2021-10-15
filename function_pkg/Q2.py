# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  15/10/2021
# Modified Date: 
# Description :
# Listening : 

# ...............................


#Encryption Logic
import time


def encrypt(password):
    result = ""
    message = ''

    #add 2 with each character value
    for i in range(len(password)):
        char = password[i]
        #print(char)
        result = chr(ord(char) + 2)
        message = message + result
    

    print("Encryption going on.....")
    time.sleep(3)
    #print final encryption code
    print("Encrypted Password is :\t"+message)




if __name__ == "__main__":

    #initial password
    password = input("enter your password :\t")
    print("My Password is :\t" + password)
    encrypt(password)




'''

   Main method of application 



   Linear programming only presented here wrt demo of lists



   Parameters:

    none



   Returns:

    none

  '''
