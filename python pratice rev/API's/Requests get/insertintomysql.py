# import csv,mysql.connector,json,requests
# dbcon=None
# #getting req.
# data=requests.get('https://jsonplaceholder.typicode.com/users')
# users=data.json()
# new_users=[]
# #extract data
# for user in users:
#     new_users.append((user['id'],user['name'],user['address']['city'],user['email']))
#     #print(new_users)
# #load data into mysql
# try:
#     dbcon=mysql.connector.connect(host='localhost',
#                                   user='root',
#                                   password='root',
#                                   database='12am')
#     cursor = dbcon.cursor()
#     sql_st='''insert into users values
#             (%s,%s,%s,%s);
#             '''
           
#     cursor.executemany(sql_st,new_users)
#     dbcon.commit()
#     print("data inserted succesfully Successfully")

# except mysql.connector.DatabaseError as err:
#     print(err.msg)

# finally:
#     cursor.close()


#adding data into the mysql table by using python code.
# import mysql.connector,requests,json
# dbcon=None
# #getting req.
# data=requests.get('https://dummyjson.com/products')
# products=data.json()
# new_products=[]
# #extract data
# for prod in products:
#     new_products.append((prod[{'id'}],prod[{'title'}],prod[{'category'}],prod['price'],prod['rating'],prod['instock']))

#     #print(new_users)
# #load data into mysql
# try:
#     dbcon=mysql.connector.connect(host='localhost',
#                                   user='root',
#                                   password='root',
#                                   database='4pmm')
#     cursor = dbcon.cursor()
#     sql_st='''insert into users values
#             (%s,%s,%s,%s,%s,%s);
#             '''
           
#     cursor.executemany(sql_st,new_products)
#     dbcon.commit()
#     print("data inserted succesfully Successfully")
# except mysql.connector.DatabaseError as err:
#     print(err.msg)
# finally:
#     cursor.close()
#     dbcon.close()


import mysql.connector,requests


# Fetch data
data = requests.get('https://dummyjson.com/products')
products = data.json() 
new_products = []
if 'products' in products:  
    for prod in products['products']:  
        new_products.append((prod['id'],prod['title'],prod['category'],prod['price'],prod['rating']))

# Load data into MySQL
try:
    dbcon = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='4pm'
    )
    cursor = dbcon.cursor()
    sql_st = '''INSERT INTO prods (id, title, category, price, rating) VALUES (%s, %s, %s, %s, %s);'''

    cursor.executemany(sql_st, new_products)  # Insert extracted data
    dbcon.commit()
    print("Data inserted successfully!")

except mysql.connector.DatabaseError as err:
    print(f"Database error: {err}")

