# 1. Countdown
count = []
def countdown(num):
    for n in range(num, 0, -1):
        count.append(n)
    return count
print(countdown(5))

# 2. Print and Return
def print_and_return(arr):
    print(arr[0])
    return arr[1]
print(print_and_return([1,2]))

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

# solution from Coding Dojo
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5. This Length, That Value
def length_and_value(size, value):
    newList = []
    while len(newList) < size:
        newList.append(value)
    return newList
print(length_and_value(6, 2))

# solution from Coding Dojo
def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))