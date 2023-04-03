# 1. Countdown
count = []
def countdown(num):
    for n in range(num, 0, -1):
        count.append(n)
    return count
print(countdown(5))

# 2. Print and Return
def print_and_return(num1, num2):
    print(num1)
    return num2
print(print_and_return(2, 4))

# 3. First Plus Length
def first_plus_length(arr):
    sum = arr[0] + len(arr)
    return sum
print(first_plus_length([1,2,3,4,5]))

# 4. Values Greater than Second
newList = []
def values_greater_than_second(arr):
    count = 0
    for num in arr:
        if len(arr) < 2:
            return 'False'
        elif num > arr[1]:
            newList.append(num)
            count += 1
    print(count)
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))

# 5. This Length, That Value
def length_and_value(size, value):
    newList = []
    while len(newList) < size:
        newList.append(value)
    return newList
print(length_and_value(6, 2))