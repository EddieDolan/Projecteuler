__author__ = 'eddie'

# i've only implemented a basic sieve (sieve of Eratosthenes)
# most efficient solution would be sieve of Atkin in C
# I may try and implement sieve of Atkin in python
# I may build my own version and test against these benchmarks

# Against most of this code is horribly inefficient, i am trying to make it easy to follow

def eddies_generator(num):
    return_list = []
    for x in range(2,int(num**.5)):
        if x not in return_list:
            if num%x == 0:
                return_list.append(x)
                return_list.append(num / x)

def eddies_generator2(num):
    factors = []
    if num == 2:
        return [2] # prime number passed in
    print num
    n = num**.5 # limiting factor to speed up program
    print n
    for x in eddies_generator2(n):
        if num % x == 0:
            divisors = eddies_generator2(x)
            if divisors == []:
                factors.append(x) # prime number passed in
            else: # unneccisary as return is above
                for y in divisors:
                    for ans in eddies_generator2(y):
                       factors.append(ans)
    return [] # prime number passed in



def Eratosthenes(num):
    # returns a list of all prime numbers up to num
    # wont work for problem 3
    nums = range(2,num + 1)
    p = 2
    q = 2
    while p != nums[-1]:
        while q < num:
            print q
            q = q + p
            if q in nums:
                nums.remove(q)
        p = nums[nums.index(p) + 1]
        q = p
    return nums

print eddies_generator2(10)