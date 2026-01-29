# def getFactors(n):
#     factors = [1, n]
#     itr = 0
#     for i in range(2, (n//2)+1):
#         if (n % i == 0):
#             factors.append(i)
#         itr += 1
#     print("Iterations for", n, itr)
#     return factors



# def getFactors1(n):
#     factors = [1]
#     itr = 0
#     for i in range(2, n+1):
#         if (n % i == 0):
#             factors.append(i)
#         itr += 1
#     print("Iterations for", n, itr)
#     return factors


# def getFactors2(n):
#     factors = []
#     itr = 0
#     i = 1
#     while (i*i <= n):
#         itr +=1
#         if (n%i==0):
#             factors.append(i)
#             if i != (n//i):
#                 factors.append(n//i)
#         i+=1
#     print("Iterations for", n, itr)
#     return factors




# print(getFactors1(10000))
# print(getFactors(10000))
# print(getFactors2(10000))




def getSumOfDigitsNPower(a, n):
    sum = 0
    while (a > 0):
        dig = a % 10
        pow = dig**n
        sum += pow
        a = a//10
    return sum


def isHappy(n):
    seen = set()
    while 1:
        n = getSumOfDigitsNPower(n, 2)
        if (n == 1):
            return True
        if (n in seen):
            print(seen)
            return False
        seen.add(n)
    return False

# print(isHappy(7))
# print(isHappy(23))
# print(isHappy(97))
# print(isHappy(68))
# print(isHappy(18))
for i in range(1,10):
    print(isHappy(i))


print(isHappy(58))
