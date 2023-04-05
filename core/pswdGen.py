import random
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class passwordGen():

    def __init__(self, upers=False, numbers=False,symboles=False) -> None:
        self.upers = upers
        self.numbers = numbers
        self.symboles = symboles
        self.password = None
        self.id = None

    def generate(self, size=8)-> str:
        """Genrate custom password with giving size"""
        upers_letters = "AZERTYUIOPQSDFGHJKLMWXCVBN"
        lowers_letters = "azertyuiopqsdfghjklmwxcvbn"
        numbers = "1234567890"
        symbols = "&(-)_=+{[]}:;,!<>@$%*§&"
        sample = lowers_letters
        if self.upers:
            sample +=upers_letters
        if self.numbers:
            sample +=numbers
        if self.symboles:
            sample +=symbols
        self.password = ''.join(random.choice(sample) for i in range(size))
        return self.password


    def generateID(self)-> str:
        upers_letters = "AZERTYUIOPQSDFGHJKLMWXCVBN"
        lowers_letters = "azertyuiopqsdfghjklmwxcvbn"
        numbers = "1234567890"
        sample = lowers_letters+upers_letters+numbers
        id = "PWD-"+''.join(random.choice(sample) for i in range(10))
        self.id = id
        return id
    
    def generateKey(self)-> None:
        key = Fernet.generate_key()
        with open("core/key.key","wb") as file:
            file.write(key)
        file.close()

    def encrypt(self, paswd=None)-> str:
        key = os.getenv("key")
        key = key.encode()
        fernet = Fernet(key)
        if paswd:
            paswd = paswd.encode()
            return fernet.encrypt(paswd)
        else:
            raise Exception("There no password generated or giving")

    def decrypt(self, paswd=None)-> str:
        key = os.getenv("key")
        key = key.encode()
        fernet = Fernet(key)
        if paswd:
            return fernet.decrypt(paswd)
        else:
            raise Exception("There no password generated or giving")
