#1. write a python program to subtract two numbers and print it
num1 = 1.5
num2 = 6.3
difference = num1 - num2
print(f'Difference: {difference}')

#2. write a python program to print 5 random integers between 10 and 20
import random
print(random.sample(range(10, 20), 5))

#3. write a python program to delete a variable
i = 10
del i

#4. write a python program to perform multiple assignments
a = b = c = 1

#5. write a python program to swap two numbers
(x, y) = (1, 2)
print(f'Before swapping: x: {x}, y: {y}')
(y, x) = (x, y)
print(f'After swapping: x: {x}, y: {y}')

#6. write a python program to print bitwise AND operation
a = 60
b = 13
a_and_b = a&b
print(a_and_b)

#7. write a python program to print bitwise OR operation
a = 60
b = 13
a_or_b = a|b
print(a_or_b)

#8. write a python program to print bitwise XOR operation
a = 60
b = 13
a_xor_b = a^b
print(a_xor_b)


#9. write a python program to print binary ones complement on a variable
a = 60
ones_complement_a = ~a
print(ones_complement_a)

#10. write a python program to print binary left shift on a variable
a = 60
binary_left_shift = a<<2
print(binary_left_shift)

#11. write a python program to print binary right shift on a variable
a = 60
binary_right_shift = a>>2
print(binary_right_shift)

#12. write a python function to check if an item exists in a list and return the boolean value
def item_exists(lst, item):
    if item in lst:
        return True
    else:
        return False

#13. write a python function to get the type of a variable 
def get_type(var):
    return(type(var))

#14. write a python function to check if an object is an instance of a given class 
def check_instance(derived_class, base_class):
    return(isinstance(derived_class, base_class))

#15. write a python function to accept user input to continue
def get_userinput():
    while(1):
        do_continue = raw_input('Do you want to continue(y/n)?')
        if do_continue == 'y' or do_continue == 'n':
            return do_continue


#16. write a python program to create a raw string
str1 = r'hello\n'

#17. write a python function to print prime numbers between two numbers 
def get_prime_numbers(range1, range2):
    for num in range(range1,range2):
        for i in range(2,num):
            if num%i == 0:
                j=num/i
                break
        else:
            print(num, 'is a prime number')

#18. write a python function to get the value of maximum integer allowed on the system 
def get_max_integer():
    import sys
    return sys.maxsize

#19. write a python function to get the absolute value of a number
def get_absolute_value(i):
    return(abs(i))

#20. write a python function to return the exponential of a number 
def get_exponential_value(i):
    import math
    return(math.exp(i))

#21. write a python function to return the natural logarithm of a number 
def get_natural_log_value(i):
    import math
    return(math.log(i))

#22. write a python function to return the base 10 logarithm of a number 
def get_natural_log_value(i):
    import math
    return(math.log10(i))

#23. write a python function to return the square root of a number 
def get_sqrt(i):
    import math
    return(math.sqrt(i))

#24. write a python program to print the maximum integer in a list of integers
lst = [23, 10, 55, 43]
lst.sort()
max = lst[-1]

#25. write a python program to print the minimum integer in a list of integers
lst = [23, 10, 55, 43]
lst.sort()
min = lst[0]

#26. write a python program to print a random number between 0 and 1
import random
print(random.uniform(0, 1))

#27. write a python program to concatenate two strings and print
str1 = 'hello'
str2 = ' world!'
print(str1 + str2)

#28. write a python program to print the ascii value of a character
str1 = 'a'
print(ord(str1))

#29. write a python program to print current date and time 
import datetime
print(datetime.datetime.now())

#30. write a python program to capitalize a string 
str1 = 'hello'
print(str1.capitalize())

#31. write a python program to clone a list
a = [1, 2, 3]
b = a[:]

#32. write a python program to print a list in reverse
a = [1, 2, 3]
print(a[::-1])

#33. write a python program to print a list in sorted order
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(sorted(basket))

#34. write a python function to return union of two sets
def union_set(set1, set2):
    return set1|set2

#35. write a python program to print a set of all elements in either set1 or set2, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))

#36. write a python program to print names of the entries in the directory given by path
path = '/home'
import os
print(os.listdir(path))

#37. write a python program to create a directory named path
path = 'test'
import os
os.mkdir(path)

#38. write a python program to add two matrices and print them
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

result = [[X[i][j] + Y[i][j]  for j in range
(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)

#39. write a python function to check if a string is a palindrome or not
def isPalindrome(s):
    return s == s[::-1]

#40. write a python program to print the least frequent character in a string
test_str = "this is test string"
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get)
print(res)

#41. write a python program to print sum of elements in a list
lst = range(5)
print(sum(lst))

#42. write python code to merge two dictionaries
def merge_dict(dict1, dict2):
    return(dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
merge_dict(dict1, dict2)
print(dict2)

#43. write python code to print temperature in celsius to fahrenheit
celsius = 37.5
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

#44. write python function to detect if a number is even number
def is_even(num):
    return((num % 2) == 0)

#45. write python function to detect if a number is odd number
def is_odd(num):
    return((num % 2) != 0)

#46. write python function to detect if an year is leap year
def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True 
            else:
                return False
        else:
            return True 
    else:
        return False 

#47. write a python program to print the largest number among the three input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

#48. write a python program to find the factorial of a number provided by the user.
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#49. write a python program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

#50. write a python program to print transpose a matrix and print
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


#51. write a python program to convert Kilometers to Miles
kilometers = float(input("Enter value in kilometers: "))

conv_fac = 0.621371

miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

#52. write a python program to check if a number is positive, negative or 0
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

#53. write a python program to check if a number is a prime number
num = int(input("Enter a number: "))

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")

#54. write a python function to find H.C.F of two numbers
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

#55. write a python python program to find the L.C.M. of two input number
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))

#56. write a python function to find the factors of a number
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

#57. write a python program to remove punctuations from a string and print it
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("Enter a string: ")

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)

#58. write a python program to count the number of each vowel and print them
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str:
   if char in count:
       count[char] += 1

print(count)


#59. write a python program to print week number from a date
import datetime
print(datetime.date(2015, 6, 16).isocalendar()[1])

from datetime import date, timedelta

def all_sundays(year):
       dt = date(year, 1, 1)
       dt += timedelta(days = 6 - dt.weekday())
       while dt.year == year:
          yield dt
          dt += timedelta(days = 7)

for s in all_sundays(2020):
    print(s)

#60. Write a Python program to get the last day of a specified year and month.
import calendar
year = 2020
month = 12 
print(calendar.monthrange(year, month)[1])

#61. Write a Python program to convert a string to datetime.
from datetime import datetime
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)

#62. Write a Python program to subtract five days from current date
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)

#63. Write a Python program to convert Year/Month/Day to Day of Year.
import datetime
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)

#64. Write a  program to split strings using split function.
string = "India is my country."
string_list = string.split(' ')
print(string_list)

#65. write a Python program to multiply two numbers and print it
num1 = 1.5
num2 = 6.3
product = num1 * num2
print(f'product: {product}')

#66. Write a Python program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

 #import datetime
import datetime

 #asking name
name = input('Type your name:')

 #asking age
age = input('Type your age:')

 #get the current year
now = datetime.datetime.now()

 #get difference between age x 100 years
diff = 100 - int(age)

 #show exactly year that user will turn 100 years old

print('Hi '+name+" you will complete 100 years in ",(now.year+diff))

#67. Write a Python program that asks the user to enter a number and Depending on whether the number is even or odd, print out an appropriate message to the user.

number = int(input("Number: "))

if number%2 == 0 and number%4 != 0:
print("Your number is even...")
elif number%4 == 0:
print("Your number is a multiple of 4")
else:
print("Your number is odd...")

#68. Write a Python program to check and print whether a triangle is valid or not

def triangle_check(l1,l2,l3):
    if (l1>l2+l3) or (l2>l1+l3) or (l3>l1+l2):
        print('No, the lengths wont form a triangle')
    elif (l1==l2+l3) or (l2==l1+l3) or (l3==l1+l2):
        print('yes, it can form a degenerated triangle')
    else:
        print('Yes, a triangle can be formed out of it')
length1 = int(input('enter side 1\n'))
length2 = int(input('enter side 2\n'))
length3 = int(input('enter side 3\n'))
triangle_check(length1,length2,length3)

#69. Write a Python program that accepts a string and calculate the number of digits and letters and print them

x = input("Enter a string! ")
d=l=0
for c in x:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1
    else:
        pass
print("Letters: ", l)
print("Digits: ", d)

#70. write a Python program to count the number of even and odd numbers from a series of numbers and print the result

x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd = even = 0
for i in x:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
        
print("Even Numbers are: ", even)
print("Odd Numbers are: ", odd)

#71. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 and print the result.

nl = []
for x in range(1500, 2700):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print("\n".join(nl))

#72. Write a python program to generate a random number between 1 and 9 (including 1 and 9) and Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
import math

x = math.floor((random.random() * 10) + 1)
guess=0
while guess != x:
    guess = int(input("Guess a number: "))
    if(guess == x):
        print("you got It!")
        print("Number is ", x)
        break
    elif(guess>x):
        print("You Guesses too high!")
    else:
        print("You guessed too low!")

#73. Write a Python program to check a triangle is equilateral, isosceles or scalene.# Note :# An equilateral triangle is a triangle in which all three sides are equal.# A scalene triangle is a triangle that has three unequal sides.# An isosceles triangle is a triangle with (at least) two equal sides.

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
 print("Equilateral triangle")
elif x != y != z:
 print("Scalene triangle")
else:
 print("isosceles triangle")

#74. Write a Python program to check whether an alphabet is a vowel or consonant

l = input("Input a letter of the alphabet: ")
if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % l)
elif l == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print("%s is a consonant." % l)

#75. Write a python program to Convert a list of characters into a string and print it : Example : # Input ['a', 'b', 'c', 'd']# Output abcd

s = ['a','b','c','d']
x = "".join(s)
print(x)

#76. Write a Python program to check whether a list contains a sublist and print True or False.

def is_Sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False
 
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1
                
                if n == len(s):
                    sub_set = True
 
    return sub_set
 
a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))

#77. Write a Python program to find common items from two lists. Example: # input# color1 = "Red", "Green", "Orange", "White"# color2 = "Black", "Green", "White", "Pink"# output# {'Green', 'White'}

color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))

#78. Write a Python program to Calculate the sum of the digits of a random three-digit number and print the result.

import random 

n = random() * 900 + 100 
n = int(n) 
print(n) 

a = n // 100 
b = (n // 10) % 10 
c = n % 10 

print(a + b + c)

#79.Write a Python program to find the area and perimeter of a right-angled triangle and print the perimeter and area.

import math 

AB = input("Length of the first leg: ") 
AC = input("Length of the second leg: ") 
AB = float(AB) 
AC = float(AC) 

BC = math.sqrt(AB  2 + AC  2) S = (AB * AC) / 2

P = AB + AC + BC 
print("Area of the triangle: %.2f" % S)
print("Perimeter of the triangle: %.2f" % P) 

#80. Write a Python program to find the greatest common divisor (GCD)(Euclidean algorithm) and print the result.

a = int(input())
b = int(input())

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

gcd = a + b
print(gcd)

#81. Write a Python program to select integers from a string and print those integers

s = input()
l = len(s)

i = 0
while i < l:
    num = ''
    symbol = s[i]
    while symbol.isdigit():
        num += symbol
        i += 1
        if i < l:
            symbol = s[i]
        else:
            break
    if num != '':
        print(num)
    i += 1

#82. Write a program to Expand and print a string like "a-z" #Example: enter first string :b # enter last string: e #Output : bcde
first = input("The first: ")
last = input("The last: ")

while first <= last:
    print(first, end='')
    first = chr(ord(first) + 1)
print()

#83. Write a Python function that returns the values   of the largest and second largest elements in the passed list.
def max2(x):
    if x[0] > x[1]:
        m1,m2 = (x[0],x[1])
    else:
        m1,m2 = (x[1],x[0])

    for i in range(2, len(x)):
        if x[i] > m1:
            m2 = m1
            m1 = x[i]
        elif x[i] > m2:
            m2 = x[i]
    return m1,m2

#84. Write a Python program to print the frequency of the elements in a list.Example:# input# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]# output# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)

#85. Write a Python program to generate all permutations of a list in Python. Example:# Input [1,2,3]# Output [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

import itertools
print(list(itertools.permutations([1,2,3])))

#86. Write a Python program to remove duplicates from a list.Example:# Input a = [10,20,30,20,10,50,60,40,80,50,40]# Output [10, 20, 30, 50, 60, 40, 80]

a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(uniq_items)

#87. Write a Python function to return the second smallest number in a list and print it.Example:# input# second_smallest([1, 2, -8, -2, 0])# output# -2

def second_smallest(numbers):
    a1, a2 = float('inf'), float('inf')
    for x in numbers:
        if x <= a1:
            a1, a2 = x, a1
        elif x < a2:
            a2 = x
    return a2
print(second_smallest([1, 2, -8, -2, 0]))

#88. Write a python program to determine the percentage of lowercase and uppercase letters in a string.
string = input()

length = len(string)

lower = upper = 0

for i in string:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1

per_lower = lower / length * 100
per_upper = upper / length * 100
print("Lower: %.2f%%" % per_lower)
print("Upper: %.2f%%" % per_upper)

#89. Write a Python program to Separate positive numbers from negative and print the positive numbers and negative numbers separately

from random import random

a = []
for i in range(7):
    n = int(random() * 20) - 10
    a.append(n)

print(a)

neg = []
pos = []
for i in a:
    if i < 0:
        neg.append(i)
    elif i > 0:
        pos.append(i)

print(neg)
print(pos)

#90. Write a python program to swap cases in a string and print. In other words, convert all lowercase letters to uppercase letters and vice versa and print the result #Example:input:InDiAaa #Output: iNdIaAA

s = input()
print(s.swapcase())

#91. Write a python program to implement bubble sort and print the result
from random import randint

N = 7
a = []

for i in range(N):
    a.append(randint(1, 20))
print(a)

for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            b = a[j]
            a[j] = a[j+1]
            a[j+1] = b

print(a)

#92. Write a python program to find whether a given number is perfect or not and print the result in boolean format(True or False)
x = int(input("Enter any no. ")) 

def perfect_number(n): 
    sum = 0 
    for x in range(1, n): 
        if n % x == 0: 
            sum += x 
    return sum == n

print(perfect_number(x))

#93. Write a python program to find and print the longest word in a sentence

string = "python java c c++ javascript pascal php"

print(string)

words = string.split()

id_longest = 0

for i in range(1, len(words)):
    if len(words[id_longest]) < len(words[i]):
        id_longest = i

print(words[id_longest])

#94. Write a python program to print all the values in a dictionary.
d =  {'a':1,'b':2,'c':3,'d':4}
print(d.values())

#95. Write a python program to print all the keys in a dictionary.
d =  {'a':1,'b':2,'c':3,'d':4}
print(d.keys())

#96. Write a python program to print a given string without spaces

s = "I love India   now I will be printed without any space"
for i in s:
    if i==' ': continue
    print(i,end='')

#97. Write a python program to print only upto the letter 't' in a given string.

s = "hi i love python"

i=0
while s[i]!='t':
    print(s[i],end='')
    i+=1

#98. Write a python program to print the length of a given string.
sample_str = "Python is good for datascience"
print(len(sample_str))

#99. Write a python program to turn every item of a list into its square.
sample_list = [1, 2, 3, 4, 5, 6, 7]
square_list =  [x * x for x in sample_list]
print(square_list)

#100. Write a python program to print a new set with all items from both sets by removing duplicates

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))