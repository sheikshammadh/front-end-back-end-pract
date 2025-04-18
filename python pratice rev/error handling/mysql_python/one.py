import mysql.connector

dbconnect=None
try:
    dbconnect=mysql.connector.connect(host='local host',user='root',password='root',database='11am')
    if dbconnect.is_connected():
        print("connected to database")
        # cur=dbconnect.cursor()
        # sql_stats='''
        #         create table employee(
        #         eid int,
        #         ename varchar(32),
        #         esal float);
        #           '''
        # cur.execute(sql_stats)
        # dbconnect.commit()
        # print("table created succesfully")
        

except mysql.connector.Error as err:
    print("error")
finally:
    pass