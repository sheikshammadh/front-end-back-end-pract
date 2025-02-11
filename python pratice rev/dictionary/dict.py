x={"a":1,"b":2,"c":3,"d":"shyam","e":123.123,"f":24,"g":"nandu"}
# print(type(x))dict
# print(x["g"])nandu
# print(x["c"])3

# print(x.get("a"))1 it gets key and gives output as value.
print(x.update({"d": 1, "e": 2}))
print(x.keys("d"))
print(x.clear("d"))
print(x.copy("d"))
print(x.fromkeys("d"))
print(x.items("d"))
print(x.pop("d"))
print(x.popitem("d"))
print(x.values("d"))