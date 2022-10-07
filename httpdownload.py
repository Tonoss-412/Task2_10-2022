import socket
import html
from urllib.parse import urlparse
s = socket.socket()

str = input(">>")
str = str.strip()

check = 1
if str[:6]== "httpdl" and str[7:11] == "-url":
    u=13
    link = ""
    while str[u]!=" ":
        link += str[u]
        u += 1
    u+=1
    if str[u]!="-" or str[u+1]!="-":
        check = 0
    else:
        u+=2
        path = ""
        while str[u]!=" " or u!=len(str-1):
            path += str[u]
            u += 1
        
        #####
        domain = urlparse(link).netloc
        s.connect((domain, 80))
        req = "GET "+pathFile+" HTTP/1.1\r\n"+"Host: "+domain+"\r\n"+"\r\n"
        s.send(req.encode())

        #####
        data = []
        res = s.recv(4096)
        while (len(res) > 0):
            data.append(res.decode())
            res = s.recv(4096)
        res = ''.join(data)

        #####
        len_image = b""
        if b"HTTP/1.1 200 OK" in res:
            for i in range(0, len(res)):
                if len_image != b"":
                    break
                if res[i:i+16] == b"Content-Length: ":
                    for j in range(i+16, len(res)):
                        if(not chr(res[j]).isdigit()):
                            len_image = res[i+16:j]
                            break
        else:
            print("Khong ton tai file anh.")
            exit(0)
        content_file = response.split(b"\r\n\r\n")[1]
        fileName = path.split('/')[-1]
        location = "/tmp/"+fileName
        open(location, "wb").write(content_file)
else:
    check = 0
if check == 0:
    print("Error")