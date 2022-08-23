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

class Users:
    def __init__(self, Ulogin, Fname,lname, parol, age, job):
        self.Ulogin = Ulogin
        self.Fname = Fname
        self.lName = lname
        self.parol = parol
        self.age = age
        self.job = job
    def str(self):
        return (self.Ulogin, self.Fname, self.lName, self.parol,self.age,self.job)

class Rigister:
    
    def rigister(Ulogin, Fname,lname, parol, age, job):
        query = f'''
            insert into datas(Ulogin, Fname,lname, parol, age, job)values
            ('{Ulogin}', '{Fname}', '{lname}', '{parol}', '{age}', '{job}')
        '''
        cursor.execute(query)
        conn.commit()

    def getById(login):
        cursor.execute(f'''
            select * from datas
            where Ulogin = '{login}'
        ''')
        return cursor.fetchall()
    
    def SignIN(Ulogin, parol):
        query = f'''
            select Ulogin, parol from datas where Ulogin='{Ulogin}' and parol = '{parol}' 
        '''
        cursor.execute(query)
        if len(cursor.fetchall()) < 1:
            return "Tizimga kirmadingiz"
        else:
            return "Tizimga kirdingiz"

    def changePassword(id, parol):
        query = f'''
            updete from dates set parol = '{parol}'
            where id = '{id}'
        '''
        cursor.execute(query)
        conn.commit()

    def updataData(login, column, newData):
        cursor.execute(f'''
            update datas set {column} = '{newData}' where Ulogin = '{login}'
        ''')

    def deleteLogin(login):
        query = f'''
            delete from datas where Ulogin  = '{login}'
        '''
        cursor.execute(query)
        conn.commit()

    def generetePassword():
        login = "adqvqjcQWCEQCLKLh23874ddcasSDFSDtv232$Q$3487238v2y39rbjd7f826!&#@^!T#*T!@(798yv2"
        s = ""
        for i in range(8):
            s += login[r.randint(i, len(login)-1)]
        return s
    def showFullData():
        cursor.execute(f'''
            select * from datas
        ''')
        return cursor.fetchall()


while True:
    print("[1]RO'YXATDAN O'TISH\n[2]SHOWDATA\n[3]UPDATE\n[4]SIGNIN\n[5]DELETEUSER\n[6]ShOWFULLDATA")
    son = int(input("Tanlang: "))
    if son > 6:
        print("Xato son kiritdingiz: \n")
    elif son == 1:
        user = Users(input("Enput login: "), input("First name: "), input("input last name: "), input("Input parol: "), input("Enter age: "), input("Enter job: "))
        Rigister.rigister(user.str()[0], user.str()[1],user.str()[2],user.str()[3],user.str()[4],user.str()[5])
    elif son == 2:
        id = input("Enter login: ")
        if len(Rigister.getById(id)) < 1:
            print("Bunqa user yuq")
        else:
            print(Rigister.getById(id))
    elif son == 3:
        login = input("Qaysi userning malumotini o'zgartirmoqchisiz: ")
        column = input("Nimani o'zgartirmoqchisiz: ")
        newData = input("Enter newData: ")
        Rigister.updataData(login, column, newData)

    elif son == 4:
        Rigister.SignIN(input("Login kiriting: "), input("Parolni kiriting: "))
    elif son == 5:
        login = input("Enter login: ")
        Rigister.deleteLogin(login)
    elif son == 6:
        res = Rigister.showFullData()
        for i in res:
            print(i)
        print()