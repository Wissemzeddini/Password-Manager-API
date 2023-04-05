from core.pswdGen import passwordGen
from dotenv import load_dotenv
import os

class password():

    def __init__(self, category, title, website, description, password) -> None:
        self.ID = passwordGen.generateID()
        self.category = category
        self.title = title
        self.website = website
        self.description = description
        self.__pswd = password

    def save_password(self):
        pass

    def all_password(self) -> list:
        pass

    def get_password(self) -> dict:
        pass

    def all_categories(self) -> list:
        pass

    def save_category(self) -> None:
        pass
