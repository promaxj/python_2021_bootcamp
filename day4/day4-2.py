import random

name_string = input("give me a name string:\ne.g.: a, b, c\n")
name_string_had_splite = name_string.split(", ")
# print(name_string_had_splite)   #its a list type
# print(len(name_string_had_splite))
# print(type(name_string_had_splite))
# print(type(len(name_string_had_splite)))    #its a int type
list_len = len(name_string_had_splite) - 1  #its a int type
# print(type(list_len))


random_number = random.randint(0, list_len)
print(f"{name_string_had_splite[random_number]} is going to buy the meal today!")