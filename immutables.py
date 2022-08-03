# mutable arrays
def append_array(element, input_arr=[]):
    input_arr.append(element)
    return input_arr


print(append_array(1, [1,2,3]))
print(append_array(1))
print(append_array(2))
print(append_array(3))
print(append_array(2, [5,2,3,1]))

# default operations
def pluss(a, b=2):
    return a + b

print(pluss(1, 4))
print(pluss(1))

# set
#    0 1..
a = [1,2,3,3,4,5,5]

#          0 1 2 3...
a_tuple = (1,2,3,3,4,5,5)
b = set(a)

print(a)
print(b)

b = 'String'
print(b)


users = ['sergii', 'julia']

def add_users(username):
    users.append(username)
    return users

print(add_users('stepan'))
print(users)