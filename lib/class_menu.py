#Class to display things
class FruitMenu:
    DATALIST=[]
    def __init__(self,data,menu="default"):
        self.DATALIST=data

    def showMenu(self,menu):
        choice=""
        if(menu=="default"):
            choice=self.defaultMenu(menu)
        if(menu=="add"):
            choice=self.nameMenu()
        if(menu=="edit"):
            choice=self.nameMenu()
        if(menu=="delete"):
            choice=self.deleteMenu()
        return choice

    def printDivider(self):
        print("------------------------------------------------------------")

    def defaultMenu(self,menu):
        print("\nFRUIT:")
        dlen=len(self.DATALIST)
        if(dlen>0):
            index=1
            for data in self.DATALIST:
                print(index,data)
                index+=1
        else:
            print("[fruit list is empty]")
        self.printDivider()
        choice=self.showOptions(menu)
        return choice

    def nameMenu(self):
        newname=""
        while(newname==""):
            newname=input("Enter new name: ")
        return newname

    def deleteMenu(self):
        choice=self.showOptions("delete")
        return choice

    def showOptions(self,menu):
        options=""
        choice=""
        optlist=[]
        if(menu=="default"):
            optlist=["a","x"]
            dlen=len(self.DATALIST)
            options="Choose an option: [A=add, X=end program] "
            if(dlen>0):
                optlist.append("e")
                optlist.append("d")
                options="Choose an option: [A=add, E=edit, D=delete, X=end program] "
        if(menu=="delete"):
            options="Proceed? [Y=yes, N=cancel]"
            optlist=["y","n"]
        if(len(optlist)>0):
            while((choice.lower() in optlist)==False):
                choice=input(options)
            
        return choice

    def getIndex(self):
        index=-1
        while(index<0 or index>=len(self.DATALIST)):
            index=int(input("Enter fruit number: "))-1
        return index
