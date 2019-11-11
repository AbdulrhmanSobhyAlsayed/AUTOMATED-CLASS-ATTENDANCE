import sqlite3

class database:
    id=""
    def __init__(self,databaseName = "database",table="users",numberOfColumn=2,columns=None):
        self.databaseName=databaseName
        self.openDatabase(self.databaseName)
        if not(self.tableFound(table)):
            print("done")
            self.createTable(table,numberOfColumn,columns)


    def openDatabase(self,databaseName='database'):
        self.database=sqlite3.connect("%s"%(databaseName+'.db'))
        self.cursor=self.database.cursor()
        return self.cursor

    def createTable(self,table="users",numberOfColumn=2,columns=None):

        print("hi")
        if not(self.tableFound(table)):
            if numberOfColumn==2:
                self.cursor.execute("CREATE TABLE %s(n INTEGER PRIMARY KEY,%s %s      NOT NULL,%s   %s    NOT NULL );"
                                    %(table,columns[0],columns[1],columns[2],columns[3]))
            elif numberOfColumn ==3:
                print("dine")
                self.cursor.execute("CREATE TABLE %s(n INTEGER PRIMARY KEY,%s %s     NOT NULL,%s   %s    NOT NULL ,%s   %s    NOT NULL );"
                                    %(table, columns[0], columns[1], columns[2], columns[3], columns[4], columns[5]))
            elif numberOfColumn==4:
                self.cursor.execute("CREATE TABLE %s(n INTEGER PRIMARY KEY,%s %s     NOT NULL,%s   %s    NOT NULL ,%s   %s    NOT NULL,%s   %s    NOT NULL );"
                                    %(table, columns[0], columns[1], columns[2], columns[3], columns[4], columns[5], columns[6], columns[7]))



    def tableFound(self,table="users"):
        print("s")
        self.cursor.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ", (table,))
        return (self.cursor.fetchone()[0] == 1)

    def insertRow(self,table,numberOfColumn=2,columns=None):
        self.openDatabase(self.databaseName)
        if numberOfColumn==2:
            self.cursor.execute("INSERT OR IGNORE INTO %s (%s,%s)  VALUES (?,?)"
                                % (table,columns[0],columns[2]),(columns[1],columns[3]))
        elif numberOfColumn==3:
            self.cursor.execute("INSERT OR IGNORE INTO %s (%s,%s,%s)  VALUES (?,?,?)"
                                % (table,columns[0],columns[2],columns[4]),(columns[1],columns[3],columns[5]))
        elif numberOfColumn==4:
            self.cursor.execute("INSERT OR IGNORE INTO %s (%s,%s,%s,%s)  VALUES (?,?,?,?)"
                                % (table,columns[0],columns[2],columns[4],columns[6]),(columns[1],columns[3],columns[5],columns[7]))

        self.database.commit()
        self.database.close()
        self.openDatabase(self.databaseName)

        print(self.databaseName +"   done")

    def select(self,table="users",number=1,array=None,relation=["AND"]):
        if number == 1:
            self.cursor.execute("SELECT * FROM %s WHERE %s =?" % (table,array[0]), (array[1],))
            return self.cursor.fetchall()
        elif number == 2:
            self.cursor.execute("SELECT * FROM %s WHERE %s =? %s %s = ? " % (table,array[0],relation[0],array[2]), (array[1],array[3]))
            return self.cursor.fetchall()
        elif number==3:
            self.cursor.execute("SELECT * FROM %s WHERE %s =? %s %s = ? %s %s =?" % (table,array[0],relation[0],array[2],relation[1],array[4]), (array[1],array[3],array[5]))
            return self.cursor.fetchall()

    def selectAll(self,table="users"):
        self.cursor.execute("SELECT * FROM %s" % (table))
        return self.cursor.fetchall()

    def idFound(self,table="users",number=1,array=None,relation=["And"]):

        return (len(self.select(table,number,array,relation))!=0)

    def deletRow(self,table="users",column="name",id="ali"):

        self.cursor.execute("DELETE  FROM %s WHERE %s =?" % (table, column), (id,))
        self.database.commit()
        self.database.close()
        self.openDatabase(self.databaseName)



