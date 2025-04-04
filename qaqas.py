#sual 75
# def count_unique(a):
#     total=0
#     for i in a:
#         b=a.count(i)
#         if b==1:
#            total = total + 1
#     return total
# user_text=input("enter list: ")
# list1=user_text.split()
# print(list1)
# print(count_unique(list1))


#sual 74
# def list_sort(a,b):
#     for j in b :
#         a.append(j)
#         b.remove(j)
#     return sorted(a)
# first_list=[]
# second_list=[]
# text1=input("enter list 1 : ")
# text2=input("enter list 2 : ")
# list1=text1.split()
# list2=text2.split()
# for i in list1 :
#     first_list.append(int(i))
# for i in list2 :
#     second_list.append(int(i))
# print(list1)
# print(list2)
# print(list_sort(list1,list2))


#sual 73
# def multiplication_table(a):
#     if a>=0:
#         for i in range(1,11):
#             b=f'{a}*{i}={a*i}'
#             print(b)
#     else:
#         c='please enter a positive number'
#         print(c)
# number=int(input("Enter a number: "))
# multiplication_table(number)


#sual 72
# def palindrome(text):
#     if ' ' in text:
#         text = text.replace(' ', '')
#     if text == text[::-1]:
#         return True
#     else:
#         return False
# a=input('enter text :').lower()
# print(palindrome(a))


#sual 71
# def average_number(a):
#     total = 0
#     for i in a:
#         total += i
#     b=total/len(a)
#     return b
# user_input = input("Enter a number list: ")
# numbers=user_input.split()
# list1=[]
# for j in numbers:
#     list1.append(float(j))
# print(average_number(list1))


#sual 70
# def count_vowel(a):
#     list1=['a','e','i','o','u','A','E','I','O','U']
#     total=0
#     for i in a:
#         if i in list1:
#             total+=1
#     return total
# text=input("enter text : ")
# print(count_vowel(text))


#sual 69
# def fibonacci(n):
#     fib = []
#     a = 0
#     b = 1
#     for i in range(n-1):
#         fib.append(a)
#         a, b = b, a+b
#     return fib
#
# number=int(input("Enter a number: "))
# print(fibonacci(number))


#sual 68
# def even_numbers(a):
#     b=[]
#     for i in a:
#         if i % 2 == 0:
#             b.append(i)
#     return b
# list1=[]
# numbers=input("Enter a number list: ")
# numbers=numbers.split()
# for i in numbers:
#     list1.append(int(i))
# print(list1)
# print(even_numbers(list1))



#sual 67
# def max_and_min(a):
#     max1=a[0]
#     min1=a[0]
#
#     for i in a:
#         if i>max1:
#             max1=i
#         if i<min1:
#             min1=i
#     print(max1,min1)
#     print(max(a), min(a))
# list1=[]
# numbers=input("Enter a number list: ")
# numbers=numbers.split()
# for j in numbers:
#     list1.append(int(j))
# print(list1)
# max_and_min(list1)


#sual 66
# def factorial(a):
#     if a < 0:
#         print('enter a positive number')
#     else:
#         b = 1
#         for i in range(1, a + 1):
#             b = b * i
#         print(b)
# number=int(input("Enter a number: "))
# factorial(number)


#sual 65
# def format_num(a):
#     formatted='{:10.2f}'.format(a)
#     return formatted
# numbers=float(input('enter number:'))
# print(format_num(numbers))


#sual 64
# def divide_numbers(a,b):
#     text='enter new number'
#     if b == 0:
#         print(text)
#     else:
#         quotient = a // b
#         remainder = a % b
#         print(f'quotient={quotient}, remainder={remainder}')
# number1=int(input('enter number 1 : '))
# number2=int(input('enter number 2 : '))
# divide_numbers(number1,number2)


#sual 63
# def round_number(a):
#     b=round(a,2)
#     return b
# number=float(input("Enter a number: "))
# print(round_number(number))


#sual 62
# def power_number(a,b):
#     pow1=pow(a,b)
#     return pow1
# x=float(input('enter a number : '))
# y=float(input('enter a number : '))
# print(power_number(x,y))


#sual 61
# def absolute_number(a):
#     b=abs(a)
#     return b
# number=int(input("Enter a number: "))
# print(f'{absolute_number(number)} : This is absolute value')


#sual 60
# def remove_suffix(a):
#     if a.endswith('.html'):
#         b=a.replace('.html','')
#         return b
#     else:
#         return a
# file_name=input('enter file name :')
# print(remove_suffix(file_name))


#sual 59
# def remove_prefix(text, prefix):
#     if text.startswith(prefix):
#         text=text.replace(prefix, '')
#         return text
#     return text
# user_text=input('enter text : ')
# user_prefix=input('enter prefix : ')
# print(remove_prefix(user_text,user_prefix))


#sual 58
# def replace_str(a):
#     if 'python' in a:
#         a=a.replace('python','JavaScript')
#         return a
# text=input('enter text : ').lower()
# print(replace_str(text))


#sual 57
# def split_str(a):
#     list1=a.split()
#     for i in list1:
#         print(i+'\n')
# text=input("enter text : ")
# split_str(text)


#sual 56
# def strip_str(a):
#     a=a.strip()
#     return a
# text=input('enter text : ')
# print(strip_str(text))


#sual 55
# def check_file(a):
#     if a.endswith('.exe'):
#         return True
#     else:
#         return False
# file_user=input('enter a file name : ')
# print(check_file(file_user))


#sual 54
# def check_prefix(a,b):
#     if a.startswith(b):
#         return True
#     else:
#         return False
# text=input('enter text : ').lower()
# prefix=input('enter prefix : ').lower()
# print(check_prefix(text,prefix))


#sual 53
# def len_str(a):
#     if a=='':
#         return 'Empty string'
#     else:
#         return len(a)
# text=input('enter text : ')
# print(len_str(text))


#sual 52
# def count_str(a,b):
#     list1=a.split(' ')
#     count1=list1.count(b)
#     return count1
# text=input("enter text : ").lower()
# word=input("enter word : ").lower()
# print(count_str(text,word))


#sual 51
# def index_str(a,b):
#     if b in a:
#         index_b1 = a.index(b)
#         index_b2 = 0
#         for i in a[::-1]:
#             print(i)
#             if i == b:
#                 index_b2 =a.index(i)
#                 break
#         return index_b1, index_b2
#     else:
#         return 'error'
# str1=input('enter string : ')
# element=input('enter element : ')
# print(index_str(str1,element))