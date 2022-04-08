# """
# Name: Darla Valderrama
# hw10.py
# """


def fibonacci(n: int):
    if n < 1:
        return None
    elif n == 1 or n == 2:
        int_using = 1
        return int_using
    elif n > 2:
        recursion_func = fibonacci(n - 1) + fibonacci(n -2)
        return recursion_func


def double_investment():
    acc = 1
    user_input = float(input("Enter your annual interest rate percentage: "))
    acc_two = 0
    while acc < 2:
        acc_two += 1
        acc = acc * (1.0 + (user_input / 100.0))
        print("The number of years it will take your principle to double is", acc_two, " years")


def syracuse(n):
    sequence = []
    sequence.append(n)
    while n!= 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = (3 * n) + 1
        sequence.append(n)
    print(sequence)


def goldbach(num):
    list_one = []
    number_one = 1
    while number_one <= num:
        counter = 0
        i = 2
        while i <= number_one // 2:
            if number_one % i == 0:
                counter = counter + 1
            i = (i + 1)
        if counter == 0 and number_one != 1:
            list_one.append(number_one)
        number_one = number_one + 1
    if num % 2 != 0:
        return None
    first_indexing = 0
    second_indexing = 0
    one_p = list_one[first_indexing]
    sec_p = list_one[second_indexing]
    while one_p + sec_p != num:
        if sec_p == list_one[-1]:
            second_indexing = second_indexing + 1
            first_indexing = first_indexing + 1
            sec_p = list_one[second_indexing]
            one_p = list_one[first_indexing]
        else:
            second_indexing = second_indexing + 1
            sec_p = list_one[second_indexing]
    return [one_p, sec_p]










