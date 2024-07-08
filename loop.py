#for loop

l = [1,2,3,4,5,6]

for i in l:
    print(i)

s = "Hello"
for j in s:
    print(j)
    
n_s = s.replace('e','a')
print(n_s)  

s1 = ""
for j in s:
    if j=='e':
        s1+='a'
    else:
        s1+=j
print(s1)

n=0 
while n < len(l):
    print(l[n])
    n+=1