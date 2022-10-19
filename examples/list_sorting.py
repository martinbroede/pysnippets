# Clarifies behaviour of lists regarding sort and reverse methods.
# Keywords:
# list / sort / key / lambda / reverse / ascending / descending

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
