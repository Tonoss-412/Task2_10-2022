import socket
import html
from urllib.parse import urlparse
s = socket.socket()

str = input(">>")
str = str.strip()

check = 1
if str[:7]== "httpget" and str[8:12] == "-url":
    u=14
    link = ""
    while str[u]!=" " or u!=len(str-1):
        link += str[u]
        u += 1

    #####
    domain = urlparse(link).netloc
    s.connect((domain, 80))
    req = "GET / HTTP/1.1\r\nHOST: "+domain+"http\r\n\r\n"
    s.send(req.encode())

    #####
    data = []
    res = s.recv(4096)
    while (len(res) > 0):
        data.append(res.decode())
        res = s.recv(4096)
    res = ''.join(data)

    #####
    title = ""
    for i in range(0, len(res)):
        if title != "":
            break
        if r[i:i+7] == "<title>":
            for j in range(i+7, len(res)):
                if res[j:j+8] == "</title>":
                    title = res[i+7:j]
                    break
    if title != "":
        print("title:", html.unescape(title))
    else:
        print("Error")
else:
    check = 0
if check == 0:
    print("Error")