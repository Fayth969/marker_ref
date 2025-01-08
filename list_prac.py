animals_con = ['lion', 'cat', 'rabbit', 'turkey', 'cat']
animals_con[1] = 'dog'
animals_con.append('goat')
#slicing
# print(animals_con[2:4])
#negative indexing
animals_con.clear()
animals_con.extend(['goat', 'cat', 'elepant'])
copy_list = animals_con.copy()
animals_con.extend(copy_list)
animals_con[2] = 'elephant'
animals_con[5] = 'elephant'
stored_count = animals_con.count("goat")
print(stored_count)
print(animals_con)
position = animals_con.index("elephant")
print('the first position of elephant is', position)
animals_con.insert(1, 'dog')
print(animals_con)