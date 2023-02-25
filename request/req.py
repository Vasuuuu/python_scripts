#!/usr/bin/python3
import requests
import webbrowser
session = requests.Session()
url = "http://webscantest.com/login.php"
#login=hello&passwd=hello123&submit_login=login
data = {"login":"testuser",
        "passwd":"testpass",
        "submit_login":"login"}
session.post(url,data=data)
r = session.get('http://webscantest.com')
file = open('file.html','wb')
file.write(r.content)
file.close()
webbrowser.open('file.html')