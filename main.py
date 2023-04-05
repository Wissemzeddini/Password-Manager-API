from core.pswdGen import passwordGen



if "__main__"==__name__:
    pwd = passwordGen(True,True,True)
    id = pwd.generateID()
    print(id)
    print("-----------------------")
    paswd = pwd.generate()
    print(paswd)
    print("-----------------------")
    enc = pwd.encrypt(paswd)
    print(enc)
    print("-----------------------")
    dec = pwd.decrypt(enc)
    print(dec)
    print("-----------------------")

