# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ..............................





#import platform module
import platform

def system_informaton():

    print(".........System Information..........  \n")

    #Returns information about bit architecture
    print("System Architecture  : ",platform.architecture())

    #Returns the Machine Type
    print("Machine              : ",platform.machine())

    #Returns Computer Network Name
    print("Node                 : ",platform.node())

    #Returns System Platform Information
    print("System Platform Info : ",platform.platform())

    #Returns OS Name
    print("Operating System     : ", platform.system())

    #Returns OS version
    print("OS Version           : ",platform.version())


system_informaton()




