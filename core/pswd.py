from core.pswdGen import passwordGen
from dotenv import load_dotenv
import sqlite3 as sql
from datetime import datetime
import os

# Load environment variables from .env file
load_dotenv()

class password():

    database = os.getenv("database")
    con = sql.connect(database)

    def __init__(self, category, title, website, description, password) -> None:
        self.ID = passwordGen.generateID()
        self.category = category
        self.title = title
        self.website = website
        self.description = description
        self.__pswd = password
    
    def sqllite_connect(self) -> object:
        return self.con.cursor()

    def setup(self) -> None:
        mycursor = self.sqllite_connect()
        if os.path.isfile(self.database):
            if not self.check():
                now = datetime.now()
                print("create table users with default login.")
                mycursor.execute("create table users(id integer primary key autoincrement, username text, password text, lastlogin datetime)")
                data = ('admin','123456789',now)
                print("create table passwords.")
                mycursor.execute("""insert into users(username,password,lastlogin) values(?,?,?)""",data)
                mycursor.execute("create table passwords(id text primary key,title text, website text null,desc text null,password text not null, createdAt datetime, updatedAt datetime)")
                self.teardown()
            else:
                print("Everything is OK table users and passwords are existe!")


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
    
    def check(self):
        mycursor = self.sqllite_connect()
        mycursor.execute("select * from users")
        res = mycursor.fetchall()
        return len(res) != 0
    
    def teardown(self) -> None:
        self.con.close()
