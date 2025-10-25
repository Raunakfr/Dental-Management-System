# Dental Management System
#Importing datetime module for use in logs and login time
import datetime
#Setting up mysql and python connection
import mysql.connector as a
fa=open("logs.txt","a+")
b=a.connect(host="localhost",user="root",passwd="090607",db="dbms")
#Creating cursor object
gg=b.cursor()
#Defining the mainscreen function to check if user wants to login as admin or guest and if admin
#checking his password else taking logs of invalid input, the password has been hardcoded for this
#program's sake, and please ignore the haphazard variable names (more to come), lack of time did me good 😭
def mainscreen():
    d=int(input("Who wants to login ?\n1. Guest\n2. Admin\nPlease enter your input(1-2): "))
    if d==1:
        print("Welcome guest")
        e=input("Do you want to see records(y/n): ")
        if e=="y":
            f=int(input("Which record do you want to see ?\n1. Patient records\n2. Employee records\nPlease enter your input(1-2): "))
            if f==1:
                seerecsg()
            elif f==2:
                seeErecsg()
            else:
                print("Invalid input")
        elif e=="n":
            print("Bye")
            exit
    elif d==2:
        g=input("Enter the password for admin access: ")
        if g==c:
            print("Successful login at\n",str(date),"\n",ctime)
            admlgn()
    else:
        al=input("Enter your name: ")
        print("Invalid password tried to be entered on"+" "+str(date)+" "+ctime+" by "+al)
        fa.write("\n"+"Invalid password tried to be entered on"+" "+str(date)+" "+ctime+" by "+al)
        print("Logs saved!")
        exit
#Defining the function to see patient records, by getting data from 'pdata' table
def seerecs():
    gg.execute("Select * from pdata")
    ss=gg.fetchall()
    print(len(ss),"records were found, here they are: ")
    for at in ss:
        print(at)
    au=input("Go back to main menu?(y/n): ")
    if au=="y":
        admlgn()
    elif au=="n":
        exit
    else:
        print("Invalid input")
#Defining the function to see employee records, by getting data from 'edata' table
def seeErecs():
    gg.execute("Select * from edata")
    av=gg.fetchall()
    print(len(av),"records were found, here they are: ")
    for aw in av:
        print(aw)
    ax=input("Go back to main menu?(y/n): ")
    if ax=="y":
        admlgn()
    elif ax=="n":
        exit
    else:
        print("Invalid input")
#Creating the interface to be shown to the user if he logins as a guest, and wants to execute a function again
#after doing it for the first time
def gstlgn():
    e=input("Do you want to see records(y/n): ")
    if e=="y":
        f=int(input("Which record do you want to see ?\n1. Patient records\n2. Employee records\nPlease enter your input(1-2): "))
        if f==1:
            seerecs()
        elif f==2:
            seeErecs()
        else:
            print("Invalid input")
    elif e=="n":
        print("Bye")
        exit
#The records panel to be shown to the guest
def seerecsg():
    gg.execute("Select * from pdata")
    h=gg.fetchall()
    print(len(h),"records were found, here they are: ")
    for i in h:
        print(i)
    j=input("Go back to main menu?(y/n): ")
    if j=="y":
        gstlgn()
    elif j=="n":
        exit
    else:
        print("Invalid input")
#A feature of admin panel which adds data to the existing tables in the database
#Uses basic loops to take input as many times as the user wants and then insert them into the table using 
#execute function alongwith the query as 'u' and the values as 'uu'
def addrecs():
    k=int(input("How many records do you want to add?: "))
    l=0
    mm=[]
    while l<k:
        n=int(input("Enter patient ID: "))
        o=input("Enter patient's name: ")
        p=int(input("Enter patient's age: "))
        q=input("Enter the name of the doctor consulted: ")
        r=input("Enter patient's address: ")
        s=int(input("Enter patient's phone number: "))
        mm.append([n,o,p,q,r,s])
        l+=1
    for t in mm:
        u=f"insert into pdata values(%s,%s,%s,%s,%s,%s)"
        uu=(t[0],t[1],t[2],t[3],t[4],t[5])
        gg.execute(u,uu)
    print("Data added!")
    b.commit()
    j=input("Go back to main menu?(y/n): ")
    if j=="y":
        admlgn()
    elif j=="n":
        exit
    else:
        print("Invalid input")
#A feature of the admin panel used to modify the existing records of any patient
#Gives options to change any data except the patient ID
def modrecs():
    w=int(input("Enter the patient id of the patient whose data has to be modified: "))
    x=int(input("What needs to be changed?\n1. Name\n2. Age\n3. Doctor Name\n4. Address\n5. Phone number\nPlease enter your input(1-5): "))
    if x==1:
        y=input("Enter new name: ")
        query1=f"update pdata set name=%s where id=%s"
        z=(y,w)
        gg.execute(query1,z)
        print("Changed!")
        b.commit()
    elif x==2:
        ac=input("Enter new age: ")
        query2=f"update pdata set age=%s where id=%s"
        ab=(ac,w)
        gg.execute(query2,ab)
        print("Changed!")
        b.commit()
    elif x==3:
        ad=input("Enter new Doctor's name: ")
        query3=f"update pdata set Docname=%s where id=%s"
        ae=(ad,w)
        gg.execute(query3,ae)
        print("Changed!")
        b.commit()
    elif x==4:
        af=input("Enter new address: ")
        query4=f"update pdata set address=%s where id=%s"
        ag=(af,w)
        gg.execute(query4,ag)
        print("Changed!")
        b.commit()    
    elif x==5:
        ah=input("Enter new phone number: ")
        query5=f"update pdata set phone_number=%s where id=%s"
        ai=(ah,w)
        gg.execute(query5,ai)
        print("Changed!")
        b.commit()
    else:
        print("Invalid input")
    aj=input("Do you want to modify more records?(y/n): ")
    if aj=="y":
        modrecs()
    elif aj=="n":
        ak=input("Go back to main menu?(y/n): ")
        if ak=="y":
            admlgn()
        elif ak=="n":
            exit
        else:
            print("Invalid input")
    else:
        print("Invalid input")
#Another admin feature which lets us delete any patient's data
def delrecs():
    am=int(input("Enter the id of the patient whose data has to be removed: "))
    query6=f"delete from pdata where id=%s"
    gg.execute(query6,am)
    b.commit()
    print("Deleted")
#Admin only feature which allows the viewing of admin data
def seeErecsg():
    gg.execute("Select * from edata")
    ap=gg.fetchall()
    print(len(ap),"records were found, here they are: ")
    for aq in ap:
        print(aq)
    ar=input("Go back to main menu?(y/n): ")
    if ar=="y":
        gstlgn()
    elif ar=="n":
        exit
    else:
        print("Invalid input")
#Admin only feature again and this allows to add more employess in the 'edata' table
#It also uses the same logic as the addrecs() function
def adderecs():
    ba=int(input("How many records do you want to add?: "))
    bb=0
    bc=[]
    while bb<ba:
        bd=int(input("Enter Employee ID: "))
        be=input("Enter Employee's name: ")
        bf=(input("Enter Employee's Profession: "))
        bg=int(input("Enter Employee's salary: "))
        bh=input("Enter Employee's address: ")
        bi=int(input("Enter Employee's phone number: "))
        bc.append([bd,be,bf,bg,bh,bi])
        bb+=1
    for bj in bc:
        bk=f"insert into edata values(%s,%s,%s,%s,%s,%s)"
        bl=(bj[0],bj[1],bj[2],bj[3],bj[4],bj[5])
        gg.execute(bk,bl)
    print("Data added!")
    b.commit()
    j=input("Go back to main menu?(y/n): ")
    if j=="y":
        admlgn()
    elif j=="n":
        exit
    else:
        print("Invalid input")
#This allows to delete the data of any employee
def delerecs():
    bk=int(input("Enter the id of the employee whose data has to be removed: "))
    query7=f"delete from edata where id=%s"
    gg.execute(query7,bk)
    b.commit()
    print("Deleted")
#Allow modificaiton of any employee's data except the employee ID
def moderecs():
    ca=int(input("Enter the patient id of the patient whose data has to be modified: "))
    cb=int(input("What needs to be changed?\n1. Name\n2. Profession\n3. Salary\n4. Address\n5. Phone number\nPlease enter your input(1-5): "))
    if cb==1:
        cc=input("Enter new name: ")
        query8=f"update edata set name=%s where id=%s"
        cd=(cc,ca)
        gg.execute(query8,cd)
        print("Changed!")
        b.commit()
    elif cb==2:
        ce=input("Enter new age: ")
        query9=f"update edata set profession=%s where id=%s"
        cf=(ce,ca)
        gg.execute(query9,cf)
        print("Changed!")
        b.commit()
    elif cb==3:
        cg=input("Enter new Doctor's name: ")
        query10=f"update edata set Salary=%s where id=%s"
        ch=(cg,ca)
        gg.execute(query10,ch)
        print("Changed!")
        b.commit()
    elif cb==4:
        da=input("Enter new address: ")
        query11=f"update edata set address=%s where id=%s"
        db=(da,ca)
        gg.execute(query11,db)
        print("Changed!")
    elif cb==5:
        b.commit()    
        de=input("Enter new phone number: ")
        query12=f"update edata set phone_number=%s where id=%s"
        df=(de,ca)
        gg.execute(query12,df)
        print("Changed!")
        b.commit()
    else:
        print("Invalid input")
    aj=input("Do you want to modify more records?(y/n): ")
    if aj=="y":
        modrecs()
    elif aj=="n":
        ak=input("Go back to main menu?(y/n): ")
        if ak=="y":
            admlgn()
        elif ak=="n":
            exit
        else:
            print("Invalid input")
    else:
        print("Invalid input")
#Admin only feature to view logs which store the login attempts with invalid password alongwith 
#the user's name and time
def viewlogs():
    fa.seek(0)
    ee=fa.read()
    print(ee)
    ak=input("Do you want to go to the main menu?(y/n): ")
    if ak=="y":
        admlgn()
    elif ak=="n":
        exit
    else:
        print("Invalid input")
#Allows the changing of the hardcoded password using basic file handling
def passchange():
    lala=input("Enter new password: ")
    abcde=open("Password.txt", "w")
    abcde.write(lala)
    abcde.close()
    admlgn()
#The basic admin panel shown to the user after succesful login/navigating and going back to the main menu
def admlgn():
    f=int(input("What do you want to do ?\n1. View patient records\n2. Add patient records\n3. Modify patient records\n4. Delete patient records\n5. View employee records\n6. Add employee records\n7. Remove employee records\n8. Modify employee records\n9. View incorrect password entered logs\n10. Change Password\n11. Logout\nPlease enter your input(1-11): "))
    if f==1:
        seerecs()
    elif f==2:
        addrecs()
    elif f==3:
        modrecs()
    elif f==4:
        delrecs()
    elif f==5:
        seeErecs()
    elif f==6:
        adderecs()
    elif f==7:
        delerecs()
    elif f==8:
        moderecs()
    elif f==9:
        viewlogs()
    elif f==10:
        passchange()
    elif f==11:
        mainscreen()
    else:
        print("Invalid input")
#Using the date time module to get the dat and time, then using basic string functions to seperate date and time
date=datetime.datetime.now().date()
time=datetime.datetime.now().time()
times=str(time)
times=times.split(".")
ctime=times[0]
#Opening the file which has the password, so that it can be used the in program to check for successful logins
abcd=open("Password.txt", "r")
abcd.seek(0)
c=abcd.read()
abcd.close()
#The main prompt which is first shown to the user as soon as he tuns the program
#Checking for either guest or admin
d=int(input("Who wants to login ?\n1. Guest\n2. Admin\nPlease enter your input(1-2): "))
#Letting guest login
if d==1:
    print("Welcome guest")
    e=input("Do you want to see records(y/n): ")
    if e=="y":
        f=int(input("Which record do you want to see ?\n1. Patient records\n2. Employee records\nPlease enter your input(1-2): "))
        if f==1:
            seerecsg()
        elif f==2:
            seeErecsg()
        else:
            print("Invalid input")
    elif e=="n":
        print("Bye")
        exit
#Tbd if password is correct
elif d==2:
    g=input("Enter the password for admin access: ")
    if g==c:
        print("Successful login at\n",str(date),"\n",ctime)
        admlgn()
#Storing logs if password is incorrect
else:
    al=input("Enter your name: ")
    print("Invalid password tried to be entered on"+" "+str(date)+" "+ctime+" by "+al)
    fa.write("\n"+"Invalid password tried to be entered on"+" "+str(date)+" "+ctime+" by "+al)
    print("Logs saved!")
    exit