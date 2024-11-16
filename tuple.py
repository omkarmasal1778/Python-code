my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

my_list.append(6)
print("List after adding an element:", my_list)

my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)

print("First element of tuple:", my_tuple[0])


my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Dictionary:", my_dict)


my_dict["age"] = 26
print("Dictionary after updating age:", my_dict)


my_set = {100, 200, 300, 400, 500}
print("Set:", my_set)

my_set.add(600)
print("Set after adding an element:", my_set)


my_set.add(300)
print("Set after trying to add a duplicate element:", my_set)
