import tkinter as tk
from dme_tools import *
from os import listdir, chdir
from os.path import dirname, abspath
import re


class ToolsWindow:
    def __init__(self) -> None:
        chdir(dirname(abspath(argv[0])))
        fontDef = ('Arial', 15)
        root = tk.Tk()
        root.title('dot-meow-encryptor')
        root.geometry('250x200')
        root.configure(background='#1A3636')
        tk.Button(text='Encrypt', background='#D6BD98', font=fontDef, command=ToolsWindow.encrypt).pack(pady=10)
        tk.Button(text='Decrypt', background='#D6BD98', font=fontDef, command=ToolsWindow.decrypt).pack(pady=10)
        tk.Button(text='Generate key', background='#D6BD98', font=fontDef, command=EncryptionTools.generateKey).pack(pady=10)
        root.mainloop()
    
    def xCrypt(encrypt:bool):
        l, p,  s  = listdir(), "catsound$", False
        for i in l:
            print(i)
            if re.search(p, i):
                s = True
                secret = i
                l.remove(i)
                print(l)
                break
        
        if not s:
            print('secret not found!')

        else:
            key = EncryptionTools.loadKey(secret)
            f = Fernet(key)
            if encrypt:
                EncryptionTools.encryptFiles(f, l)
                print('Encrypted!')
            else:
                EncryptionTools.decryptFiles(f, l)
                print('Decrypted!')

    def encrypt():
        ToolsWindow.xCrypt(True)

    def decrypt():
        ToolsWindow.xCrypt(False)


if __name__ == '__main__':
    t = ToolsWindow()