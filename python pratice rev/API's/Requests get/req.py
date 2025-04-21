# Gettinfg responce:
# import mysql.connector,requests,json,csv
# dbcon=None
# data=requests.get('https://jsonplaceholder.typicode.com/users')
# users=data.json()
# new_users=[]
# for user in users:
#     new_users.append((user['id'],user['name'],user['address']['city'],user['email']))
#     print(new_users)


import mysql.connector
dbcon=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='12am')
    cursor = dbcon.cursor()
    sql_st='''insert into users values
            '''
           
    cursor.executemany(sql_st,)
    dbcon.commit()
    print("data inserted succesfully Successfully")

except mysql.connector.DatabaseError as err:
    print(err.msg)

finally:
    pass