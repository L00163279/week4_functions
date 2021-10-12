# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................


def lyit_lnum(lnum):

    print(f'Hi, {lnum}')
    print(id(lnum))
    lnum = 5456
    print(lnum)
    print(id(lnum))
    #return

def lyit_name(name):
    fname , lname = str(name).split(" ")
    print(f'Hi {fname} {lname}, Welcome to Lyit')
    #return


if __name__ == "__main__":
    lyit_name("muhammed SHafeeq")
    abc = lyit_lnum("l1234")
    print(id(abc))




'''

   Main method of application 



   Linear programming only presented here wrt demo of lists



   Parameters:

    none



   Returns:

    none

  '''
