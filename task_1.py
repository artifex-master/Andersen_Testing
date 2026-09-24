
# Enter the starting value
value = input("Введите некотрое число: ")

#Split the numeric char values for a string value in an array
def split_str_literals(value):
    numbers = []
    current = ""
    for char in value:
        if char.isdigit():
            current += char
        else:
            if current:
                numbers.append(int(current))
                current = ""
    if current:
        numbers.append(int(current))
    return numbers

# Find out thouse numbers in an array which is multiple of 3
def is_multiple_of_3(numbers):
    output_arr = []
    for num in numbers:
        if num % 3 == 0:
            output_arr.append(num)
    print(output_arr)

# Take initial value and check if it is equal to John then output 'Hello John', otherwise check if it is a singular number
# check if it is greater than 7 or less than 7
# On line 38, check if it is an array. If that's an array, go through the array and output only those which is multiple of 3
if value == "John":
    print("Hello John!")
elif value.isnumeric():
    if int(value) > 7:
        print("Hello")
    else:
        print("No value")
else:
    is_multiple_of_3(split_str_literals(value))













