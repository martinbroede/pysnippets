# Creation and usage of dictionaries.
# Keywords:
# dict / dictionary / comprehension / key / value / item

# Basics -->

my_dict = {
    "123": 'hello',
    "987": 'world',
}

print("values:", ' '.join(my_dict.values()))
# values: hello world
print("keys:", ' '.join(my_dict.keys()))
# keys: 123 987
print(my_dict.pop('123'))
# hello
print(my_dict['987'])
# world
my_dict.update({'456': 'is', '123': 'beautiful'})
print(my_dict)  # 'hello' has been popped!
# {'987': 'world', '456': 'is', '123': 'beautiful'}

# Dict comprehension -->

vowels = ('a', 'e', 'i', 'o', 'u')
sentence = 'this sentence has some vowels'
vowel_counter = {key: sentence.count(key) for key in vowels}  # dict comprehension
# = {'a': 1, 'e': 5, 'i': 1, 'o': 2, 'u': 0}
print("\n".join(f"{key}:{value}" for (key, value) in vowel_counter.items()))  # another comprehension
