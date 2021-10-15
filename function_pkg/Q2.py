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
def encrypt(password):
    result = ""
    message = ''

    #add 2 with each character value
    for i in range(len(password)):
        char = password[i]
        #print(char)
        result = chr(ord(char) + 2)
        message = message + result


    #print final encryption code
    print("Encrypted Password is :"+message)




if __name__ == "__main__":

    #initial password
    password = "mypassword"
    print("My Password is :" + password)
    encrypt(password)




'''

   Main method of application 



   Linear programming only presented here wrt demo of lists



   Parameters:

    none



   Returns:

    none

  '''
