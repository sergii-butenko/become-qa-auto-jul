a = 10  # primitive
b = a - 5 ## <---- 5

str_a = "sergii"
str_b2 = str_a.replace('i', 'e')

list_a = [1,3,4]
list_b = list_a.append(5)

print(list_a)
print(list_b)






hashable_tuple = (1,2,3)
non_hashable_list = [1,2,3]

print(hashable_tuple)
print(non_hashable_list)

a_dict = {
    non_hashable_list: "sergii"
}

print(a_dict[non_hashable_list])
