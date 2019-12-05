import pymysql
i = 9
id = i
os ='Microsoft Windows 7 旗舰版'
# db = pymysql. connect( host=' 192.168.1.224', user=' root ’, password='admin ', port=3306, db='web-flash')

db = pymysql.connect(host='192.168.1.224', user='admin', password='admin', port=3306)

cursor = db.cursor()
sql = 'INSERT INTO epsmachineinfo(id, os) values(%s, %s) '
try:
    cursor.execute(sql,(id, os))
    db.commit()
except:
    db.rollback()
db.close()