
# import mysql.connector
# dbcon=None
# try:
#     dbcon=mysql.connector.connect(host='localhost',
#                                   user='root',
#                                   password='root',
#                                   database='11am')
#     cursor = dbcon.cursor()
#     sql_st='''
#             create table employee(
#             eid int,
#             ename varchar(32),
#             esal float
#             );
#            '''
#     cursor.execute(sql_st)
#     dbcon.commit()
#     print("Table Created Successfully")

# except mysql.connector.DatabaseError as err:
#     print(err.msg)

# finally:
#     pass


# import mysql.connector
# dbcon=None
# try:
#     dbcon=mysql.connector.connect(host='localhost',
#                                   user='root',
#                                   password='root',
#                                   database='11am')
#     cursor = dbcon.cursor()
#     sql_st='''insert into employee values(101,"shyam",45000),(102,"sham",45000),
#     (103,"shya",45000),(103,"hyam",45000)'''
           
#     cursor.execute(sql_st)
#     dbcon.commit()
#     print("data inserted succesfully Successfully")

# except mysql.connector.DatabaseError as err:
#     print(err.msg)

# finally:
#     pass


# Getting responce from API's


import requests
data=requests.get('https://jsonplaceholder.typicode.com/users')
users=data.json()
print(users)

