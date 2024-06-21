#integers

x = 10
A = -10
y = 0


#floats

a = 1.5
b = -1.5
c = 0.0

#basic operations
# to perform basic arithmetic operations with numbers

sum = x + y 
sub = A - a 
mul = a * b
div = a / b

#exponentiation

expo = a ** x

#modulus

mod = x % 2

#integer division

int_div = x // a 


#string

s1 = 'Hi there!'
s2 = "Hello World!"

print(s1 + "\n" + s2) # new line & concatenation

s3 = '''
This is an example
of 
multi line.
'''

print(s3)

#repetition

rep = s1 * 5

print(rep)

#repetition with new line 

rep1 = [s1] * 5 # created a list 
rep1_str = "\n".join(rep1) 
print(rep1_str)

# character accessing

# Hello World!
# 012345678910

f_char = s2[0]
print(f_char)
l_char = s2[11]
print(l_char)
ll_char = s2[-2]

print(ll_char)

# slicing 

# Hello World!

sub_s2 = s2[0:5]
sub1_s2 = s2[6:14]
print(sub_s2)
print(sub1_s2)


#Length

length = len(s2)
print(length)

#Some Methods

# Hello World!

to_upper = s2.upper()
to_lower = s2.lower()
to_split = s2.split()

print(to_upper)
print(to_lower)
print(to_split)

#list
#empty list

empty_list = []

#list with elements

l1 = [1,2,3,4,5,6]
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])
print(l1[5])

print(l1[-1])
print(l1[-5])


#slicing in list

print(l1[2:6])
print(l1[2:5])
print(l1[2:])

#changing item in a list

l2 = [10,20,30,40,50,60]
print(l2)
l2[2] = 90
print(l2)


#adding items in a list

#append

l2.append('hello') # append দ্বারা কোনোকিছু সংযুক্ত করা হয় তবে তা লিস্ট এর শেষে যুক্ত হবে !
print(l2)

#insert

l2.insert(4,'hello')
print(l2)

#extend
l2.extend([9,8,7,6,5,4])
print(l2)

l2.extend(l1)
print(l2)