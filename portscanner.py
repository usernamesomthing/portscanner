import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )



host = input("Provide the IP you want to scan: ")
port = int(input("Port you want to scan: "))
timeouttime = int(input("How long do you want to scan before timeout: "))



def portScanner(port):
    s.settimeout(timeouttime)
    if s.connect_ex((host, port)):
        print("This port is closed :( ")
    else:
        print("This port is open!")
portScanner(port)
