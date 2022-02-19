import math

# need to know for upcoming test ...
result = math.sqrt(9)
print(result)
# will return data type float ...

res = math.pow(2, 3)  # two to the third
res_1 = 2 ** 3
print(res, res_1, end='!')

print(list(range(10)))
# returns sequence 0-9
# range can take up to three parameters

my_range = range(0, 10)
# starts at 0 and runs until hits 10 but does not count 10 itself, #range(10)
my_range = range(3, 10) # range(3,10, 1)
my_range = range(3, 10, 2) # range goes by two
# <<< [3, 5, 7, 9]
my_range = range(10, 3, -2)
# start at 10, count till 3, and then go backwards -2 subtract

# range(start, stop, step)
# start defaults to 0
# step defaults to 1

my_range = range(3.5)
# range func requires integers ...

my_range = range(0, 10*2)
    for i in my_range:
        print(i / 2)
# returns range in .5 halfs ...



# accumulator pattern
# when looping something want to add/accumulate results like adding all num up to 10 for ex ...
sum = 0
# initialize variable
for i in range(101):
    sum = sum + i
print(sum)
# >>> 5050

# variable is 0, first time thru value 0, then 1, then 2, and continue looping
# 0 + 0 setting that result


fact = eval(input("Enter values to factorialL: "))
acc = 1
for i in range(fact, 0, -1)
# say start at 6, go down to 0 not including 0, and count down by negative -1
    acc = i * acc
print(acc)

list(range(6, 0, -1))
[6, 5, 4, 3, 2, 1]




