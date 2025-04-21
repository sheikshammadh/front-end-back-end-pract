import csv,mysql.connector,json,requests
dbcon=None
#getting req.
data=requests.get('https://jsonplaceholder.typicode.com/users')
users=data.json()
new_users=[]
#extract data
for user in users:
    new_users.append((user['id'],user['name'],user['address']['city'],user['email']))
    #print(new_users)
#load data into mysql
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='12am')
    cursor = dbcon.cursor()
    sql_st='''insert into users values
            (%s,%s,%s,%s);
            '''
           
    cursor.executemany(sql_st,new_users)
    dbcon.commit()
    print("data inserted succesfully Successfully")

except mysql.connector.DatabaseError as err:
    print(err.msg)

finally:
    cursor.close()

