import socket
import time
from notify import *
import a_star

#goal state

host, port = "127.0.0.1", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

startPos = [-9.3,1.25,-4.94] #Vector3   x = 0, y = 0, z = 0
Location = {'A':[-9.3,1.25,-4.94],
            'B':[-9.3,1.25,-8],
            'C':[-5.91,1.25,-7],
            'D':[1.92,1.25,-2.64],
            'E':[2.52,1.25,-9.6],
            'F':[9.38,1.25,-0.57],
            'G':[9.38,1.25,-9.86],
            'H':[-2.44,1.25,0.28],
            'I':[-9.54,1.25,0.24],
            'J':[-9.54,1.25,7.15],
            'K':[-3.5,1.25,9.55],
            'L':[0.75,1.25,9.55],
            'M':[9.34,1.25,4.46],
            'N':[9.3,1.25,9.55]}
# # print(Location['A'])
def simulate(address,pickup,sender_ph,reciever_ph):
    try:
        # address = input("Enter address : ")
        key = pickup.capitalize()
        print( "Source ",Location[key])
        des = address.capitalize()
        print( "Destination : ",Location[des])
        # connect(Location[key])
        # time.sleep(20)
        # notify_sender()
        # dest(Location[des])
        # time.sleep(15)
        # notify_recevier()
        path = a_star.a_starr('A',key)
        p = a_star.a_starr(key,des)
        print(f'path => to reach source :{path}')
        print(f'path => to reach destination :{p}')
        
        move(key,des,sender_ph,reciever_ph)
        return True
    except KeyError:
        print("Please check the address")
        return False
    
def move(key,des,sender_ph,reciever_ph):
    connect(Location[key])
    # time.sleep(15)
    notify_sender(sender_ph)

    dest(Location[key],Location[des])
    # time.sleep(15)
    notify_recevier(reciever_ph)

def connect (src):
    startPos = [-9.3,1.25,-4.94]
    i=0
    if startPos != src :
        while(i<9):
            time.sleep(2)
            startPos = src
            posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
            print(f'Going to {posString}')
            sock.sendall(posString.encode("UTF-8")) #Converting string to Byte, and sending it to C#
            receivedData = sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
            print(receivedData)
            i=i+1
    else:
        print("reached Pickup")

            

def dest (src,des):
    startPos =src
    j=0
    if startPos != des :
        while(j<6):
                time.sleep(2)
                startPos = des
                posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
                print(posString)
                sock.sendall(posString.encode("UTF-8")) #Converting string to Byte, and sending it to C#
                receivedData = sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
                print(receivedData)
                j=j+1
    else:
        print("reached Destination")

    


