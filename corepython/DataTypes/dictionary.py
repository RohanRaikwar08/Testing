# from timeit import default_timer
#
# dict_example = {'a': 1, 'b': 2, 'c' : 3,'d' : 4}
#
# dict_example.clear()
# print("dictionary after clear():",dict_example)
#
#
# dict_example = {'a': 1, 'b': 2, 'c' : 3,'d' : 4}
# dict_copy=    dict_example.copy()
# print("Dictionary copy:", dict.copy)
#
#
# keys = ['e', 'f','g']
# default_value = 0
# new_dict = dict.fromkeys(keys, default_value)
# print('New dictionary with fromkey():',new_dict)
#
#
# print("Value for key 'b':", dict_example.get('b'))
#
#
# print("dictionary items:",dict_example.items())
#
#
# print("Dictionary keys :",dict_example.keys())
#
#
# popped_value = dict_example.pop('b')
# print("pooped value for key 'b':", popped_value)
# print("Dictionary after pop():", dict_example)
#
#
# last_items = dict_example.popitem()
# print("popped last items:", last_items)
# print("Dictionary after popitem()", dict_example)
#
#
# print("Value for key 'z' with setdefault:" , dict_example.setdefault('z',100))
# print("Dictionary after setdefault():", dict_example)
#
#
# new_data= {'x': 10, 'y': 20}
# dict_example.update(new_data)
# print("dictionary after update():", dict_example)
#
#
#
# print("dictionary values:", dict_example.values())



dict_example = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4}

dict_example.clear()
print("dictionary after clear():", dict_example)


dict_example = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4}
dict_copy =         dict_example.copy()
print("dictonary copy:", dict_copy)



keys = ['e','f','g']
default_value =0
new_dict = dict.fromkeys(keys, default_value)
print(" new dictionary with fromkeys():", new_dict)



print("value for keys 'b':", dict_example.get('b'))


print("dictionary items:", dict_example.items())


print("dictionary keys:", dict_example.keys())


popped_value = dict_example.pop('b')
print("popped value for key'b':", popped_value)
print("dictionary after pop():", dict_example)


last_items = dict_example.popitem()
print("popped last items:", last_items)
print("dictionary after popitem():", dict_example)


print("value for key 'z' with setdefault:", dict_example.setdefault('z', 100))
print("dictionary after setdefault():", dict_example)


new_data = {'x':10, 'y': 20}
dict_example.update(new_data)
print("dictionary after update():", dict_example)