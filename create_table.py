import pyodbc
server = 'zhmeishi.database.windows.net'
database = 'bigdatathon'
username = 'zhmeishi'
password = 'Comp3111h'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)



with open('ChineseRestaurant.csv',encoding="utf-8-sig") as csv_file:
    Restreader = csv.reader(csv_file)
    header = next(Restreader)
    RestList=list(Restreader)

for k in RestList:
    try:
        cursor1 = cnxn.cursor()
        cursor1.execute("INSERT INTO resturant (name, price_ui, review_count, url) VALUES(N'{}', '{}', {}, '{}');".format(k[0],k[1],k[2],k[3]))
        cursor1.commit()
    except Exception as e:
        print('duplicated entry:{}'.format(k[0]))
