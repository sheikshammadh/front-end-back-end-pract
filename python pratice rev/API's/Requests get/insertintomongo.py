import requests,pymongo
#Extract Data
products=requests.get('https://dummyjson.com/products').json()['products']
#print(type(products))  # <class 'list'>

#DB Connection
client = pymongo.MongoClient('mongodb://localhost:27017/')
db=client['12pm']
product_col=db['prods']
product_col.insert_many(products)
print("Product data writen success")