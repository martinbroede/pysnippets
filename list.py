# Creation and usage of lists.
# Keywords:
# list / append / extend / insert / pop / len

my_list = ['A', 1]  # list elements can have arbitrary types
my_list += ['a', 'Z']  # you can concatenate lists like strings
# the line above equals my_list.extend(['a', 'Z'])
print(my_list.pop())  # pop last item of list (standard pop behaviour in LIFO structures)
# Z
print(my_list.pop(0))  # pop first item of list
# A
my_list.append("last")
my_list.insert(0, "first")  # 'prepend'
my_list.remove('a')
print(my_list)
# ['first', 1, 'last']
print(my_list * 2)  # concatenate list with itself
# ['first', 1, 'last', 'first', 1, 'last']
