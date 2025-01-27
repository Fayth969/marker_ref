new__list = []
fruit_tuple = ('apple', 'banana', 'mango', 'guava', 'mango', 'pineapple', False, True)
# print(fruit_tuple[1])
# convert from tuple to a list
convert_list = list(fruit_tuple)
convert_list[3] = 'melon'
# converting from list to a tuple
fruit_tuple = tuple(convert_list)
# print('new result : ', fruit_tuple , 'length of my  tuple is :', len(fruit_tuple))
# if 'mango' not in fruit_tuple:
#     print('yes mango is a member of fruit')
# else:
#     print('mango is not a member of fruit')
if 'apple' in fruit_tuple :
    fruit_tuple = list(fruit_tuple)
    change_false = int(fruit_tuple[6])
    chnge_true = int(fruit_tuple[7])
    fruit_tuple[6] = change_false
    fruit_tuple[7] = chnge_true
    fruit_tuple = tuple(fruit_tuple)
    print(fruit_tuple)
else :
    print(False)
print(fruit_tuple.count("mango"))
print(fruit_tuple.index('pineapple'))