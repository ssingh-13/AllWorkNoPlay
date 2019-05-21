# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
from datetime import datetime as dt #now we don't have to use datetime.datetime

hosts_temp = 'hosts'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts' #using r allows escaping escape characters
redirect = '127.0.0.1'
distractions = ['www.facebook.com', 'facebook.com', 'www.amazon.com', 'www.shein.com']
#these 4 elements need their own respective linesnon the host file and redirect IP
print(dt.now())
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 21) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
#We created 3 datetime objects and compared them, to add our time window
        print('Working hours: ')
        with open(hosts_path, 'r+') as file:
#Using r+ allows to raed and write in a file
            content = file.read() #this will load the entir file
            for site in distractions:
                if site in content:
                    pass
                else:
                    file.write(redirect + ' ' + site + '\n')
    else:
        with open(hosts_path, 'r+') as file:
#the readline method will produce a list with each str item
#then check the readlines list against our sites in distractions list and if items them, I want them out, but no method to delete the append list
            content = file.readlines()
#once readlines is complete the pointer will point to the very end of the file
#so any append method will add from the point of the pointer
#the seek method will point pointer where we want
            file.seek(0)
            for line in content:
#if item not there, append a new file hosts via writing a new file
                if not any(site in line for site in distractions):
                    file.write(line)
#truncate method will delete all things UNDER the specified sections
            file.truncate()
        print('Back in action!!')
    time.sleep(60)
        
