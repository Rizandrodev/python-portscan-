import socket
import sys

portas=[21,22,80,443,8080,3306,3000,5173]

for port in range(1,65536):
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meusocket.settimeout(0.5) #assincronismo
    code=meusocket.connect_ex((sys.argv[1],port))
    # if code=0 porta aberta  se for 111 fechado 
    if code ==0:
        print(port,"porta aberta")
    # else:
    #     print(code,port)
