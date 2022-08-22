import psycopg2
from faker import Faker
fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    database="datas",
    user="datas",
    password="1"
)

cursor = conn.cursor()

class Rigister:
    def __init__(self, Ulogin, Fname,lname, parol, age, job):
        self.Ulogin = Ulogin
        self.Fname = Fname
        self.lName = lname
        self.parol = parol
        self.age = age
        self.job = job
    def writeDatabase(self):
        query = f'''
            insert into datas(Ulogin, Fname,lname, parol, age, job)values
        '''
    def rister(self):
        pass
    def showData(self):
        pass
    def signIN(self):
        pass
    def getById(self):
        pass
    def checkLoginAndCHeckParol(self):
        pass
    def changePassword(self):
        pass
    def deleteLogin(self):
        pass
    def updeteLoginANDParol(self):
        pass

print("HEllo")