# age = 42
# if age > 40:
#     print("Your over the hill")
# else:
#     print("Your still a youngun")


# x = 25
# if x > 40:
#     print("Your over the hill")
# elif x == 20:
#     print("Your still a baby")
# else:
#     print(x)

# for num in range(1, 5, 1):
#     print(num)

# for num in range(0, 25, 5):
#     print(num)

# for num in range(25, 0, -5):
#     print(num)

# for(num = 0; num > 25; num++)
# (let num = 25; num>0; num--)


# list = ["Hello", "Houston", "Happy", "Humpday"]
# for i in range(0, len(list)): # for loop
#     print(list[i])
#     print(i+1, list[i])

y = 24
# while y < 24:
#     print(y)
#     y = y -1
# else:
#     print("Printing")


# Functions


# JS Version
# function add(a, b) {
#     return a + b
#     console.log(a + b)
# }
# add(2, 4)

def add(a,b):
    x = a + b
    return x
    print(x)

# add(2,4)

# 0-500000 odd numbers add together them and print final sum
# sum = 0
# for x in range(1, 500000, 2):
#     sum = sum + x

# print(sum)
# This above is done during learning or test environments as it is always active or will always run


# This is how you would call it in real world so that it is only activated or run when called on like a submit button
def finalSum():
    sum = 0
    for i in range(1, 500000, 2):
        sum += i
    print(sum)
# finalSum()
