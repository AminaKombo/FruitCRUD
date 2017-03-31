#FRUITCRUD
'''
Simple text-based CRUD for a fruit database
'''
import sys
from lib.class_dbconnector import DbConnector
from lib.class_menu import FruitMenu
fruitlist=[]
dbcon=DbConnector('dbinfo.txt')
menu=FruitMenu(fruitlist)
cursor=dbcon.CURSOR

def populateFruits():
    global cursor, dbcon, fruitlist
    fruitlist=[]
    try:
        cursor.execute("SELECT fruit FROM fruit ORDER BY fruit ASC")
        for fruit in cursor.fetchall():
            fruitlist.append(fruit[0])
    except:
        print("Error: could not reach database.")

def fruitExists(fruit):
    global dbcon, cursor
    verdict=False
    fruit=fruit.lower()
    try:
        cursor.execute("SELECT COUNT(*) FROM fruit WHERE fruit=%s",(fruit))
        cn=cursor.fetchone()[0]
        if(cn>0):
            verdict=True
    except:
        print("Error: could not search database.")
    return verdict

def addFruit(newfruit):
    global dbcon, cursor
    newfruit=newfruit.lower()
    if(fruitExists(newfruit)==False):
        try:
            cursor.execute("INSERT INTO fruit(fruit) VALUES(%s)",(newfruit))
            dbcon.DB.commit()
            print("New fruit added:",newfruit)
        except:
            print("Error: could not save record")
            dbcon.DB.rollback()
    else:
        print(newfruit, "exists")
        
def editFruit(index,newname):
    global dbcon, cursor, fruitlist
    newname=newname.lower()
    if(fruitExists(newname)==False):
        try:
            cursor.execute("UPDATE fruit SET fruit=%s WHERE fruit=%s",\
                           (newname,fruitlist[index]))
            dbcon.DB.commit()
            print("Fruit updated:",newname)
        except:
            print("Error: could not save record")
            dbcon.DB.rollback()
    else:
        print(newname, "exists")

def deleteFruit(index):
    global dbcon, cursor, fruitlist
    fruit=fruitlist[index]
    try:
        cursor.execute("DELETE FROM fruit WHERE fruit=%s",(fruit))
        dbcon.DB.commit()
        print("Fruit deleted:",fruit)
    except:
        print("Error: could not delete record")
        dbcon.DB.rollback()

def handleChoice(choice):
    global menu, fruitlist, dbcon
    if(choice=="a"):
        newfruit=menu.showMenu("add")
        addFruit(newfruit)
        startApp()
    if(choice=="e"):
        index=-1
        menu.DATALIST=fruitlist
        index=menu.getIndex()
        menu.printDivider()
        print("now editing: ",fruitlist[index].upper())
        newname=menu.showMenu("edit")
        editFruit(index,newname)
        startApp()
    if(choice=="d"):
        index=-1
        menu.DATALIST=fruitlist
        index=menu.getIndex()
        menu.printDivider()
        print("up for deletion: ",fruitlist[index].upper())
        choice=menu.showMenu("delete")
        if(choice=="y"):
            deleteFruit(index)
        startApp()
    if(choice=="x"):
        dbcon.DB.close()
        exit()

def startApp():
    global menu, fruitlist
    populateFruits()
    menu.DATALIST=fruitlist
    choice=menu.showMenu("default")
    handleChoice(choice.lower())

startApp()

