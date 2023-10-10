# cat = "asdf"


# print(cat)

# cat = "catcatcat"
# dog = cat + "12"

# print(cat)

# cat = 13

# print(cat)

# dog = cat + 12

# print(dog)

# print(type(dog))

# print(1 is not 2)

a = 'abc'
b = 'abc'

print(a is b)
print(id(a))
print(id(b))

c = 1231234983149872
d = 1231234983149871
print(c is d)
print(id(c))
print(id(d))

if (a == b) :
    print("되냐")
else :
    print("안되냐")

e = 1

for i in range(0,10):
    print(i)


f = [a,b,c]

for i in f:
    print(i)

if (c>d):
    for i in range(0,5):
        print(i)
else:
    for i in range(6,10):
        print(i)




def plus(a, b):
    return a + b


print(plus(10,2))