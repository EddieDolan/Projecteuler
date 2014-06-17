__author__ = 'eddie'


def euler1(num_max):
    temp_list =[]
    for x in range(100):
        if x%5==0:
            temp_list.append(x)
        elif x%3==0:
            temp_list.append(x)
    return sum(temp_list)

print euler1(100)


print sum([x for x in range(100) if x%3==0 or x%5==0])

b = []
for x in range(10):
    if x%5==0:
        b.append(x*2)
print b

a =  [x*2 for x in range(10)]
print a

c = [x for x in range(10) if x%5==0]
print c