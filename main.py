import pyodbc


conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\hzgra\PycharmProjects\WriteOdd\AccessVeritabaniVeriKaydetmeVeOkuma\vt1.accdb;')
cursor=conn.cursor()
cursor.execute('SELECT * FROM Tablo1')

for row in cursor.fetchall():
    print(row)

conn.close()

