import sqlite3 as sql
con =  sql.connect('organizationdb.sqlite')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')
Fname = input('File name: ')
if (len(Fname) < 1): Fname ='C:/Users/kiran/PycharmProjects/Coursera/Database/mbox.txt'
fopen = open(Fname)
for line in fopen :
    if not line.startswith('From:'):continue
    data = line.split()[1]
    email = data.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?',(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts(org,count) VALUES (?,1)''',(email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(email,))
        con.commit()
sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
cur.close()