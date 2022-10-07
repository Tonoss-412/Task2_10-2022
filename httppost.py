import socket
import html
from urllib.parse import urlparse
s = socket.socket()

str = input(">>")
str = str.strip()

check = 1
if str[:8]== "httppost" and str[9:13] == "-url":
    u=15
    link = ""
    while str[u]!=" ":
        link += str[u]
        u += 1
    u+=1
    if str[u]!="-":
        check = 0
    else:
        u+=1
        username = ""
        while str[u]!=" ":
            username += str[u]
            u += 1
        u+=1
        if str[u]!="-":
            check = 0
        else:
            u+=1
            password = ""
            while str[u]!=" " or u!=len(str-1):
                password += str[u]
                u += 1

            #####
            domain = urlparse(link).netloc
            body = "log="+username+"&pwd="+password+"&wp-submit=Log+In"
            s.connect((domain, 80))
            req = "POST /wp-login.php HTTP/1.1\r\n"+"HOST: "+domain + "\r\n"+"Content-Length: "+str(len(body))+"\r\n"+"Content-Type: application/x-www-form-urlencoded"+"\r\n"+"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"+"\r\n"+"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"+"\r\n" + "Cookie: wordpress_test_cookie=WP Cookie check; wp_lang=en_US"+"\r\n" \
            "\r\n"+body
            s.send(req.encode())


            #####
            data = []
            res = s.recv(4096)
            while (len(res) > 0):
                data.append(res.decode())
                res = s.recv(4096)
            res = ''.join(data)


            #####
            if "HTTP/1.1 302 Found" in res and "is incorrect" not in res and "is not registered on this site" not in res:
                print("User "+username+" dang nhap thanh cong.")
            else:
                print("User "+username+" dang nhap that bai.")
else:
    check = 0
if check == 0:
    print("Error")