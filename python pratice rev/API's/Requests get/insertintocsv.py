import csv,mysql.connector,json,requests
dbcon=None
#getting req.
data=requests.get('https://jsonplaceholder.typicode.com/users')
users=data.json()
# new_users=[]
fp=open('user.csv','w',newline='null')
csvwriter=csv.write(fp)
csv


