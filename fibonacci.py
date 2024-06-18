# first two terms: 0 & 1
print("How many numbers should I enter")
num = int(input())
a, b = 0, 1
count = 2
print(a)
print(b)

#fiding the first 10 fibonacci numbers
while count <= num:
    c = a+b
    print(c)
    count = count + 1
    a=b+c
    print(a)
    count = count + 1
    b = a
    a = c
    

