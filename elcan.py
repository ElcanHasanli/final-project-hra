##############################################################################################################
#51
# write a python function that takes a string and a character as input and returns the first and last occurrence index of the character in the string. If the character is not found, return -1.
# Question: What is the difference between startswith() and endswith() in python
# def find_first_last_occurrence(s, char):
#     if char not in s:
#         raise ValueError(f"Character '{char}' not found in the string.")  # Error if char not in string
#
#     first_index = s.index(char)  # Find the first occurrence
#     last_index = s[::-1].index(char)  # Reverse string and find the index from end
#     last_index = len(s) - 1 - last_index  # Convert to original index
#
#     return first_index, last_index
#
#
# # Example usage
# s = "hello world"
# char = "o"
# print(find_first_last_occurrence(s, char))  # Output: (4, 7)
# text = "python proqramlaşdırma"
#
# print(text.startswith("python"))  # True (sətir "python" ilə başlayır)
# print(text.endswith("ma"))        # True (sətir "ma" ilə bitir)
# print(text.startswith("pro", 7))  # True (7-ci indeksdən sonra "pro" ilə başlayır)

####################################################################################################
#52
# def count_word_occurrences(sentence, word):
#     sentence = sentence.lower()  # Cümləni kiçik hərfə çevir
#     word = word.lower()  # Sözün özünü də kiçik hərfə çevir
#     words_list = sentence.split()  # Cümləni sözlərə ayır
#     return words_list.count(word)  # Sözün neçə dəfə təkrarlandığını tap
#
# # Nümunə istifadəsi
# sentence = "Python çox güclü bir dildir. Python proqramlaşdırma çox maraqlıdır."
# word = "python"
# print(count_word_occurrences(sentence, word))  # Çıxış: 2


# import re
#
# def count_partial_word_occurrences(sentence, word):
#     sentence = sentence.lower()  # Kiçik hərfə çevir
#     word = word.lower()
#     matches = re.findall(word, sentence)  # Sözün cümlədə neçə dəfə keçdiyini tap
#     return len(matches)  # Neçə dəfə tapıldığını qaytar
#
# # Nümunə istifadəsi
# sentence = "Caterpillar və cat eyni kökə malikdir. Cat sevgililəri üçün maraqlı bir mövzudur."
# word = "cat"
# print(count_partial_word_occurrences(sentence, word))  # Çıxış: 3
####################################################################################################
# #53
# Write a Python function that takes a string as input and returns its length. If the string is empty, return a message saying "Empty string".
# Question:What does len() return for a list, and how is it different from its use with strings?
# def count_unique_elements(lst):
#     return len(set(lst))
#
# # Test edək
# my_list = [1, 2, 2, 3, 4, 4, 5]
# print(count_unique_elements(my_list))  # 5
#
#
#
# my_list = [1, 2, 3, 2, 4]
# print(my_list.index(2))  # 1 (çünki ilk 2-ci element 1-ci indeksdədir)
# my_list = [1, 2, 3, 2, 4]
# print(my_list.count(2))  # 2 (çünki 2 iki dəfə var)
####################################################################################################

#54
# Write a Python function that checks if a given string starts with a user-specified prefix. The function should be case-insensitive.
# Question: What is the difference between tuple() and list()?
# def starts_with_prefix(text, prefix):
#     return text.lower().startswith(prefix.lower())
#
# # Test
# print(starts_with_prefix("Hello World", "hello"))  # True
# print(starts_with_prefix("Python Programming", "py"))  # True
# print(starts_with_prefix("Data Science", "code"))  # False

# Tuples yaddaşı daha effektiv idarə etdiyi üçün böyük verilənlərdə daha optimaldır. Listlər isə dəyişikliklər tələb olunan hallarda daha uyğundur.

####################################################################################################

#55
# def is_txt_file(filename):
#     return filename.lower().endswith(".txt")
# print(is_txt_file("doc.txt"))
####################################################################################################

#56
# write a python function that removes leading and trailing spaces from a user-inputted string and prints the cleaned string
# def clean_string(user_input):
#     cleaned = user_input.strip()
#     print(cleaned)
# clean_string("    Hello, world     ")
# def split_and_print(sentence):
#     words = sentence.split()  # Boşluqlara görə bölür, əlavə boşluqları avtomatik silir
#     for word in words:
#         print(word)
#
# # Misallar
# split_and_print("Hello, how are you?")
# # Hello,
# # how
# # are
# # you?
#
# split_and_print("  Python   is    great!  ")
# # Python
# # is
# # great!
#
# split_and_print("")  # Boş sətir verildikdə heç nə çap etmir
####################################################################################################

#57

# # Description:Write a python function that takes a sentence as input and splits it into a list of words. Print each word on a new line.
# def split_and_print(sentence):
#     words = sentence.split()
#     for word in words:
#         print(word)
# split_and_print('hello, how are you')
# def example_function(*args, **kwargs):
#     print("args:", args)
#     print("kwargs:", kwargs)
#
# example_function(1, 2, 3, name="Elcan", age=20)
####################################################################################################
#58
# write a python function that takes a sentence as input and replaces all occurrences of the word "Python" with "JavaScript".
# def replace_python_with_js(sentence):
#     return sentence.replace("Python", "JavaScript").replace("python", "JavaScript").replace("PYTHON","JavaScript")
# import re
# def replace_python_with_js_v2(sentence):
#     return re.sub(r'(?i)\bpython\b',"JavaScript",sentence)
# print(replace_python_with_js_v2("i love python"))
# import re
# def replace_first_python(sentence):
#     return re.sub(r'(?i)\bpython\b', "JavaScript", sentence, count=1)
#
# # Misallar
# print(replace_first_python("Python is awesome. Python is powerful."))
# # "JavaScript is awesome. Python is powerful."
####################################################################################################

#59
# write a python function that takes a string and removes a user-specified prefix if it exists.
# def remove_prefix(text, prefix):
#     if text.startswith(prefix):
#         return text[len(prefix):]
#     return text
#
# # Example usage:
# print(remove_prefix("HelloWorld", "Hello"))  # Output: "World"
# print(remove_prefix("PythonProgramming", "Java"))  # Output: "PythonProgramming"

# num = "55234"
# print(f"Starts with 55: {num.startswith('55')}")  # Using f-string
#
# # OR
# print("Starts with 55:", num.startswith("55"))  # Using a comma
####################################################################################################
#60
 # write a python function that removes a .html suffix from a given filename if it exists.
# def remove_html_suffix(filename):
#     if filename.lower().endswith('.html'):
#         return filename[:-5]
#     return filename
# print(remove_html_suffix("index"))
# t = (1, 2, 3)
# lst = list(t)  # Tuple-i list-ə çeviririk
# lst[1] = 99  # Elementi dəyişirik
# t = tuple(lst)  # Yenidən tuple-ə çeviririk
# print(t)  # (1, 99, 3)

####################################################################################################
#61
# def absolute_value(num):
#     abs_value = abs(num)  # Sayının müsbət dəyərini tapır
#     return "this is absolute value {}".format(abs_value)  # Nəticəni formatda qaytarır
#
# # Funksiyanı sınaqdan keçirmək
# print(absolute_value(-5))  # Çıxış: this is absolute value 5
# print(absolute_value(3))   # Çıxış: this is absolute value 3
# ##
# num = 3.14159
# rounded_num = round(num, 2)  # Bu, ədədin yalnız 2 onluq rəqəmini saxlayacaq
# print(rounded_num)  # Çıxış: 3.14
####################################################################################################
#62
# write a python function that calculates x^y. The function should take x and y as user inputs.
# def power_calculation():
#     try:
#         x = float(input("enter the base (x):"))
#         y= float(input("enter the exponent (y): "))
#         result = x ** y
#         print(f"{x}^{y} = {result}")
#     except ValueError:
#         print("Inavlid input!")
# power_calculation()
#
# print(pow(2, 3, 5))  # (2^3) % 5 = 3
# print(2 ** 3)  # 8
####################################################################################################
#63
# Write a python function that rounds a floating-point number to 2 decimal places. The function should take a number as input and return the rounded value.
# def round_to_two_decimals():
#     try:
#         num = float(input("enter number:"))
#         rounded_num = round(num,2)
#         return rounded_num
#     except ValueError:
#         return "invalid!"
# print(round(3.14159, 2))  # 3.14
# print(round(9.999, 2))  # 10.0
# print(round(7.5, 2))  # 7.5
# age = 20
# message = "I am " + str(age) + " years old."
# print(message)
# # Çıxış: I am 20 years old.
####################################################################################################
#64
# Write a python function that takes two integers as input and returns both the quotient and remainder.
# def quotient_and_remainder():
#     try:
#         x = int(input("enter (x):"))
#         y = int(input("enter (y):"))
#         if y == 0:
#             return "error!"
#         quotient = x // y
#         remainder = x % y
#         return quotient,remainder
#     except ValueError:
#         return "Invalid!"
# result = quotient_and_remainder()
# print(result)
####################################################################################################
#65
# write a python function that takes a floating-point number and prints it in a formatted way using the format() function.
# Format the number to 2 decimal places and align it to the right within a 10-character width.
# def format_float():
#     try:
#         num = float(input("enter:"))
#         formatted_num = "{:>10.2f}".format(num)
#         print(formatted_num)
#     except ValueError:
#         print("Invalid!")
# format_float()
#
# # String-i bayt formatında çap etmək
# text = "Python"
# byte_text = text.encode('utf-8')
#
# print(byte_text)  # Çıxış: b'Python'
####################################################################################################
#66
 # write a python function that calculates the factorial of a given positive integer using a loop. if the input is negative, print an error message
# def calculate_factorial():
#     try:
#         n= int(input("enter:"))
#         if n<0:
#             print("error.")
#         elif n == 0:
#             print("factorial of 0 is 1")
#         else:
#             factorial = 1
#             for i in range(1,n+1):
#                 factorial *= i
#             print(f"factorial of {n} is {factorial}")
#     except ValueError:
#         print("invalid!")
# calculate_factorial()
####
# 0-dan 4-ə qədər dövr edir
# for i in range(5):
#     print(i)
# # Şərt doğru olduğu müddətcə dövr edir
# i = 0
# while i < 5:
#     print(i)
#     i += 1
####################################################################################################
#67
 # write a python function that takes a list of numbers and returns the maximum and minimum values in two ways.
# def find_max_min(nums):
#     if not nums:
#         return "error!"
#     max_val = max(nums)
#     min_val = min(nums)
#     return (max_val,min_val)
# numbers = [3,7,1,9,5]
# result = find_max_min(numbers)
# print("using max() and min():",result[0])
######
# String dəyişdirilə bilməz (immutable) və yalnız simvollardan ibarətdir.
#
# List isə dəyişdirilə bilər (mutable) və müxtəlif növ verilənləri saxlaya bilər.

####################################################################################################
#68
 # Description:Write a python function that filters out and returns only the even numbers from a list using a loop.
# def filter_even_numbers(numbers):
#     even_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers
# print(filter_even_numbers([1,2,3,4]))
# keys = ('name', 'age' ,'city')
# values =('elcan', 20, 'baku')
# dictionary = dict(zip(keys, values))
# print(dictionary)

##### Tuple listəsi
# my_tuples = [("a", 1), ("b", 2), ("c", 3)]
#
# # Dictionary yaratmaq
# my_dict = dict(my_tuples)
#
# print(my_dict)
####################################################################################################
#69
 # Write a python function that generates the first n numbers of the fibonacci sequence, where nn is proived by the user.

# def fibonacci(n):
#     if n<1:
#         return []
#     elif n == 1:
#         return [0]
#     fib_seq = [0,1]
#     for _ in range(2,n):
#         fib_seq.append(fib_seq[-1] + fib_seq[-2])
#
#     return fib_seq
# print(fibonacci(10))
####################################################################################################
#70
# def count_vowels(s):
#     vowels = 'aeiou'
#     count=0
#     for char in s.lower():
#         if char in vowels:
#             count+=1
#     return count
#
# print(count_vowels("Helloo world"))
#####
# num = 123
# num_str = str(num)
#
# print(num_str)  # "123"
# print(type(num_str))  # <class 'str'>
####################################################################################################
#71
 # def average(numbers):
#     if not numbers:
#         return 0
#     return sum(numbers) / len(numbers)
# print(average([]))
###
# set 1 = ...
# set 2= ...
# my set = set 1 .union set2
####################################################################################################
#72
# Description:Write a python function that checks whether a given strings is a palindrome (reads the same forward and backward). Ignore case and spaces.
# def is_palindrome(s):
#     # Boşluqları silirik və hərfləri kiçik ediririk
#     s = s.replace(" ", "").lower()
#
#     # String-in əksinə çevrilməsini əldə edirik
#     return s == s[::-1]
#
#
# # Misal:
# print(is_palindrome("A man a plan a canal Panama"))  # True
# print(is_palindrome("Hello World"))  # False
####################################################################################################
#73
# def multiplication_table(n):
#     if n <= 0:
#         print("musbet eded daxil et")
#
#         return
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")
# multiplication_table(5)
# multiplication_table(-1)
# #
# // tam bolmedir / adi  bolmedir
####################################################################################################
#74
# Write a Python function that takes two lists of integers, merges them into a single list, and returns the merged list sorted in ascending order.
# def merge_and_sort(list1, list2):
#     merged_list = list1 + list2
#     return sorted(merged_list)
# list_a = [5,3,8]
# list_b = [7,2,6]
# print(merge_and_sort(list_a,list_b))
# numbers = [3, 1, 4, 2]

# numbers.sort()  # Mövcud siyahını sıralayır
# print(numbers)  # [1, 2, 3, 4]
# numbers = [3, 1, 4, 2]
#
# sorted_numbers = sorted(numbers)  # Yeni siyahı qaytarır
# print(sorted_numbers)  # [1, 2, 3, 4]
# print(numbers)  # [3, 1, 4, 2] (dəyişməz qalır)
####################################################################################################
#75
# # Write a Python function that takes a list and returns the count of unique elements in the list.
# def count_unique_elements(lst):
#     return len(set(lst))

# my_list = [1,2,2,3,4,4,5]
# print(count_unique_elements(my_list))
# index ve count ferqi odurki index reqemin necenci indexde oldugunu gosterir, count nece defe tekrarlandigini gosterir