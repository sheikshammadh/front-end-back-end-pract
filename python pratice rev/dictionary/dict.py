x={"a":1,"b":2,"c":3,"d":"shyam","e":123.123,"f":24,"g":"nandu",}
# print(type(x))dict
# print(x["g"])nandu
# print(x["c"])3

# print(x.get("a"))1 it gets key and gives output as value.
# x.update({"h":12344})
# print(x.update) This line would print the method reference for update, but it's not a useful operation. The correct operation is to print the dictionary after updating.
# print(x.keys()) dict_keys(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# print(x.clear()) None (This line prints all the keys in the dictionary x.)
# print(x.copy()) {'a': 1, 'b': 2, 'c': 3, 'd': 'shyam', 'e': 123.123, 'f': 24, 'g': 'nandu'}
new_dict=x.fromkeys(["a","b","c"],1)
# print(new_dict) {'a': 1, 'b': 1, 'c': 1}
# print(x.items()) dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 'shyam'), ('e', 123.123), ('f', 24), ('g', 'nandu')])
# y = x.pop("e") 123.123
# print(y)
# print(x)  

# print(x.popitem("g","shyam"))
# print(x.values())
# ====================================================================================
# # update():
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# thisdict.update({"model":"ecosport"})
# thisdict.update({"brand":"ford"})

# print(thisdict)#{'brand': 'ford', 'model': 'ecosport', 'year': 2020}
# =====================================================================================
# Accessing Items:
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]#mustang
# x=thisdict["brand"]#ford
# x=thisdict["year"]#1964
# print(x)
# =================================================================================
# Get Keys
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.keys()

# print(x)#dict_keys(['brand', 'model', 'year'])
# ===========================================================================
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()# here we getting values, if we want keys replace values into keys.
# print(x)#dict_values(['Ford', 'Mustang', 1964])
# car["color"] = "white"
# print(x)#dict_values(['Ford', 'Mustang', 1964, 'white'])
# car ["millage"]="1234567"
# print(x)#dict_values(['Ford', 'Mustang', 1964, 'white', '1234567'])
# =====================================================================================


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.items()
# print(x)#([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# =====================================================================================================
# Check if "model" is present in the dictionary:
# thisdict = {
#   "brand": "Ford",
#   "type": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
# else:
#     print("no there is no model")
# =============================================================================================================
