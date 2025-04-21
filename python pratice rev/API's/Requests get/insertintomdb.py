#inserting data into the mongodb collection
import csv,mysql.connector,json,requests
from pymongo import MongoClient
dbcon=None
#getting req.
data=requests.get('https://jsonplaceholder.typicode.com/users')
users=data.json()
new_users=[]
#extract data
for user in users:
    new_users.append((user['id'],user['name'],user['address']['city'],user['email']))
    #print(new_users)
#load data into mongodb
try:
    client = MongoClient('localhost', 27017)
    db = client['12am']
    collection = db['users']
    
    # Insert the data into the MongoDB collection
    for user in new_users:
        document = {
            'id': user[0],
            'name': user[1],
            'city': user[2],
            'email': user[3]
        }
        collection.insert_one(document)
    
    print("Data inserted successfully into MongoDB")

except Exception as err:
    print(err)
finally:
    client.close()