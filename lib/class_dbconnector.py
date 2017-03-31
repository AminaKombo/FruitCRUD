#Establishes database connection from supplied file
import pymysql

class DbConnector:
    DBHOST=""
    DBUSER=""
    DBPASS=""
    DBNAME=""
    
    def __init__(self, dbfilename):
        self.DBFILENAME=dbfilename
        self.MESSAGE=self.establishConnection()
        print(self.MESSAGE)


    def establishConnection(self):
        message=""
        try:
            self.DBFILE=open(self.DBFILENAME,'r')
            self.CONNFIELDS=list(self.DBFILE)
            message=self.removeNewLines()
            if(message!=""):
                message=self.setProperFields()
                if(message==""):
                    message=self.actualConnecting()
        except:
            message="Error finding file: "+self.DBFILENAME
        return message


    def setProperFields(self):
        #print("setting proper fields")
        message=""
        for field in self.CONNFIELDS:
            splitfield=field.split("=")
            if(splitfield[0]=="dbhost"):
                self.DBHOST=splitfield[1]
            if(splitfield[0]=="dbuser"):
                self.DBUSER=splitfield[1]
            if(splitfield[0]=="dbpass"):
                self.DBPASS=splitfield[1]
            if(splitfield[0]=="dbname"):
                self.DBNAME=splitfield[1]
        checkList=[self.DBHOST,self.DBUSER,self.DBPASS,self.DBNAME]
        blanks=0
        for checker in checkList:
            #print(checker)
            if(checker==""):
                blanks+=1
        if(blanks>0):
            message="database connection fields cannot be blank."
        return message

    
    def removeNewLines(self):
        #print("removing new lines")
        index=0
        message=""
        for thing in self.CONNFIELDS:
            thing=thing.replace("\n","")
            self.CONNFIELDS[index]=thing
            index+=1
            message="new lines removed."
        return message

    def actualConnecting(self):
        #print("actually connecting")
        try:
            self.DB=pymysql.connect(self.DBHOST,self.DBUSER,self.DBPASS,self.DBNAME)
            self.CURSOR=self.DB.cursor()
            message="Connection established to database: "+self.DBNAME
        except:
            message="Error connecting to database."
        return message


#dbcon=DbConnector('dbinfo.txt')
