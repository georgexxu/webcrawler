import pyodbc
server = 'zhmeishi.database.windows.net'
database = 'bigdatathon'
username = 'zhmeishi'
password = 'Comp3111h'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor2 = cnxn.cursor()
#cursor2.execute("CREATE TABLE person2 (PersonID int,LastName NVARCHAR,FirstName varchar(255),Address varchar(255),City varchar(255) );")
#cursor1 = cnxn.cursor()
#cursor1.execute("INSERT INTO person2 (PersonID, LastName, FirstName, Address, City) VALUES(2, N'z', 'b', 'c', 'd');")
#row = cursor1.fetchone()
#while row:
#    print (str(row[0]))
#    row = cursor1.fetchone()
#cursor1 = cnxn.cursor()
#cursor1.execute("UPDATE persons SET LastName = 'c' WHERE LastName = 'a';")
#cursor2.commit()
#cursor1.commit()
cursor = cnxn.cursor()
cursor.execute("select * from resturant;")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()