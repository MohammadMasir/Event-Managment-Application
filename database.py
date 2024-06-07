import pymysql as abc
try:
    mycon = abc.connect(host = 'localhost',user = 'root', password = 'root',port=3307,charset='utf8',db = 'student')
    print('connected')
    cur = mycon.cursor()
    cur.execute('show databases')
    for j in cur:
        print(j)
    #cur.execute('use student')
    cur.execute('show tables')
    for i in cur:
        print(i)
    cur.execute('select * from customer_details')
    result = cur.fetchall()
    for k in result:
        print(k)
except Exception as e:
    print('Error is:',e)
    

