# banking management system (bms)
from ast import Delete
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'sql',
    database = 'bank1'
)

def openacc():
    name = input('enter the customer name: ')
    accno = input('enter account no: ')
    dob = input('enter the dob: ')
    address = input('enter the address: ')
    contact = int(input('enter the contact number: '))
    balance = int(input('enter the balance: '))

    data1 = (name, accno, dob, address, contact, balance)
    sql1 = ('insert into account values (%s, %s, %s, %s, %s, %s)')

    data2 = (name, accno, balance)
    sql2 = ('insert into amount values (%s, %s, %s)')
    
    x = mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print ('data entered sucessfully')
    main()

def depoamo():
    amount = input('enter the amount you want to deposit: ')
    ac = input('enter the account number: ')
    a = 'select Balance from amount where Accno = %s'
    data = (ac,) # , is there because in single entity in a tuple we need to put comma, we use tuple so that data cannot b e edited
    x = mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()
    t = result[0] + int(amount)
    sql = ('update amount set Balance = %s where Accno = %s')
    d = (t,ac)
    x.execute (sql,d)
    mydb.commit()
    print ('amount deposited sucessfully')
    main()

def withdrawamount():
    amount = input('enter the amount to be withdrawn: ')
    ac = input('enter the account number: ')
    a = 'select Balance from amount where Accno = %s'
    data = (ac,) 
    x = mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()
    t = result[0] - int(amount)
    sql = ('update amount set Balance = %s where Accno = %s')
    d = (t,ac)
    x.execute (sql,d)
    mydb.commit()
    print ('amount withdrawn sucessfully')
    main()

def balenq():
    ac = input('enter the account number to check the balance: ')
    a = 'select Balance from amount where Accno = %s' 
    x = mydb.cursor()
    x.execute(a,ac)
    result = x.fetchone()
    mydb.commit()
    print (result)
    main()

def disdetails():
    ac = input('enter the account number to see all details: ')
    x = mydb.cursor()
    x.execute(ac)
    result = x.fetchall()
    mydb.commit()
    print (result)
    main()
def closeacc():
    ac = input('enter the account number to close that account: ')
    x = mydb.cursor()
    x.execute(ac)
    result = x.Delete()
    mydb.commit()
    print (result)
    main()

def main ():
    print('''
        1. OPEN NEW ACCOUNT
        2. DEPOSIT AMOUNT
        3. WITHDRAW AMOUNT
        4. BALANCE ENQUIRY
        5. DISPLAY CUSTOMER DETAILS
        6. CLOSE AN ACCOUNT''')
    choice = input('enter the task you want to perform: ')
    if(choice == '1'):
        openacc()
    elif(choice == '2'):
        depoamo()
    elif(choice == '3'):
        withdrawamount()
    elif(choice == '4'):
        balenq()
    elif(choice == '5'):
        disdetails()
    elif(choice == '6'):
        closeacc()
    else:
        print('invalid choice')
        main()
main()
