import pyodbc
server = 'zhmeishi.database.windows.net'
database = 'bigdatathon'
username = 'zhmeishi'
password = 'Comp3111h'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor2 = cnxn.cursor()
cursor2.execute("CREATE TABLE resturant (name NVARCHAR(32),price_ui varchar(32),review_count int, url varchar(255),instagramCount int, PRIMARY KEY (name));")
cursor1 = cnxn.cursor()
cursor1.execute("INSERT INTO resturant (name, price_ui, review_count, url, instagramCount) VALUES(N'樂天皇朝', '$101-200', 498, 'https://www.openrice.com/zh/hongkong/r-%E6%A8%82%E5%A4%A9%E7%9A%87%E6%9C%9D-%E9%8A%85%E9%91%BC%E7%81%A3-%E7%B2%B5%E8%8F%9C-%E5%BB%A3%E6%9D%B1-%E4%B8%AD%E5%BC%8F%E5%8C%85%E9%BB%9E-r170063', 0);")
cursor2.commit()
cursor1.commit()
