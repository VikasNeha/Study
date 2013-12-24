import cx_Oracle

ip = '208.109.108.8'
port = 1521
SID = 'XE'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)

conn = cx_Oracle.connect('watdata', 'Dv_WAT_99', dsn_tns)

cursor = conn.cursor()

cursor.execute('''
SELECT OWNED_MINORITY
FROM SUPPLIER
WHERE SUPPLIER_ID = :supplier_id''', supplier_id=12)

row = cursor.fetchone()

str = row[0]

if str == 'Y':
    print "123"
else:
    print "abcd"

conn.close()
