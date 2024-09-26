import socket
import sys

portas = [21, 22, 80, 443, 8080, 3306, 3000, 5173]
host = sys.argv[1]

for port in range(1, 65536):
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meusocket.settimeout(0.5)
    code = meusocket.connect_ex((host, port))
    
    if code == 0:
        meusocket.connect((host, port))
        try:
            banner = meusocket.recv(1024).decode().replace("\n","")
        except:
            banner = "Nao identificado"
        
        print(port, banner)
        
        meusocket.close()
