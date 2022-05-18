def convert(list):
    return tuple(list)

list = [1, 2, 3, 4]
converted = convert(list)
print(type(list))
print(type(converted))

def convertThroughLoop(list):
    return tuple(i for i in list)

new_list = [1, 2, 3, 4]
new_list_converted = convertThroughLoop(new_list)
print(type(new_list))
print(type(new_list_converted))

def convertThroughComma(list):
    return (*list, )

new_list2 = [1,2,3,4]
new_list2_converted = convertThroughComma(new_list2)
print(type(new_list2))
print(type(new_list2_converted))