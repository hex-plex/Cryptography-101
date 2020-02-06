#!/usr/bin/env python

import os 
from cryptography.fernet import Fernet
import keypass
key=keypass.password2key()
files=os.listdir(os.getcwd()+'/crypt/')
os.chdir(os.getcwd()+'/crypt/')
for i in files:
    fil = open(i,'r')
    encryptdata = fil.read()
    fil.close()
    os.remove(os.getcwd()+'/'+i)
    f = Fernet(key)
    try:
	data = f.decrypt(encryptdata)
        fil = open(i[:-8],'w')
        fil.write(data)
        fil.close()
    except:
	print("Extraction Failed")
   

    
    
