dict1 = {
    "a": "castle",
    "b": "water",
    "c": "soil"
    }

#to get the value of an key : 
castle = dict1.get("a") # or castle = dict1["a"]
print(castle)


#meth1 : by using : .keys() -> key
for key in dict1.keys():
    print(key + "->" + dict1[key])

#meth2 : by using : .values()
for value in dict1.values() :
    print(value)

#meth3 : by using .items() -> tupple
for item in dict1.items() :
    print(item) #its a tupple

for key , value in dict1.items() :
    print(key, "->" , value) #its a tupple


#remove an item b : water
del dict1["b"]
print(dict1)

#remove all items : .clear()
dict1.clear()
print(dict1)

dict2 = dict1.copy()
dict1["a"] = 123
print(dict2)


