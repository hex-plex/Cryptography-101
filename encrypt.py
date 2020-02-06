#!/usr/bin/env python

import os 
from cryptography.fernet import Fernet
import keypass
key=keypass.password2key()
files=os.listdir(os.getcwd()+'/crypt/')
os.chdir(os.getcwd()+'/crypt/')
for i in files:
    fil = open(i,'r')
    data = fil.read()
    fil.close()
    os.remove(os.getcwd()+'/'+i)
    f = Fernet(key)
    encryptdata = f.encrypt(data)
    fil = open(i+'.encrypt','w')
    fil.write(encryptdata)
    fil.close()


    
    
