# Clarifies behaviour of lists regarding sort and reverse methods.
# Keywords:
# list / sort / sorted / key / lambda / reverse / ascending / descending

# Note that my_list.sort() and my_list.reverse() change the original list while returning None.

my_list = [("a", 3), ("c", 1), ("b", 2)]
# [('a', 3), ('c', 1), ('b', 2)]

my_list.reverse()
# [('b', 2), ('c', 1), ('a', 3)]

my_list.sort(key=lambda s: s[0])  # same as my_list.sort() in this example.
# [('a', 3), ('b', 2), ('c', 1)]


my_list.sort(key=lambda s: s[1])  # lists are sorted ascending by default.
# [('c', 1), ('b', 2), ('a', 3)]

my_list.sort(key=lambda s: s[1], reverse=True)  # sort descending
# [('a', 3), ('b', 2), ('c', 1)]

# The builtin function sorted(iterable) returns a sorted list while not touching the original.
sorted(my_list, reverse=True)
# [('c', 1), ('b', 2), ('a', 3)]

print(my_list)  # my_list stayed untouched.
# [('a', 3), ('b', 2), ('c', 1)]
