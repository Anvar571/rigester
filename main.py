import psycopg2
from faker import Faker
fake = Faker()
import random as r

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
    def rigister(self):
        query = f'''
            insert into datas(Ulogin, Fname,lname, parol, age, job)values
            ('{self.Ulogin}', '{self.Fname}', '{self.lName}', '{self.parol}', '{self.age}', '{self.job}')
        '''
        cursor.execute(query)
        conn.commit()

    def getById(self, id):
        query = f'''
            select * from datas
            where id = '{id}'
        '''
        cursor.execute(query)

    def signIN(self, login, parol):
        if login == self.returnLoginPassword()[0] {
            print("O'tdingiz")
        }

    def returnLoginPassword(self, Ulogin, parol):
        query = f'''
            select Ulogin, parol from datas where Ulogin='{Ulogin}' and parol = '{parol}' 
        '''
        cursor.execute(query)
        return cursor.fetchall()[0]

    def changePassword(self, id, parol):
        query = f'''
            updete from dates set parol = '{parol}'
            where id = '{id}'
        '''
        cursor.execute(query)
        conn.commit()

    def deleteLogin(self, id):
        query = f'''
            delete from datas where id = '{id}'
        '''
        cursor.execute(query)
        conn.commit()

    def generetePassword():
        login = "adqvqjcQWCEQCLKLh23874ddcasSDFSDtv232$Q$3487238v2y39rbjd7f826!&#@^!T#*T!@(798yv2"
        s = ""
        for i in range(8):
            s += login[r.randint(i, len(login)-1)]
        return s

lst = []
for i in range(10):
    user = Rigister(fake.name().split()[1], fake.name().split()[0], fake.name().split()[1], fake.password(), r.randint(10, 80), fake.job())
    lst.append(user)

for i in lst:
    i.rigister()

print(Rigister.returnLoginPassword("Cantu", "^wmUF&pkk7"))