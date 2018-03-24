import time
from datetime import datetime as dt

#hosts_path = r"C:\Windows\System32\drivers\etc"   # for Mac and Linux the path would be : /etc/hosts
host_temp = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com",'facebook.com','www.businessinsider.in','businessinsider.in']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
    #if 8 < dt.now().hour < 20:
        print("Working Hours...")
        with open(host_temp,'r+') as file:

            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website+"\n")



    else:
        with open(host_temp,'r+') as file:
            content = file.readlines()
            file.seek(0) # taking pointer before the first character in the file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() # delete rest of data after writing to file once
        print("fun hours...")
    time.sleep(5)
