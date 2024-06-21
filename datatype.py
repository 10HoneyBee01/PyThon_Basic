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



