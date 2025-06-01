# TYPE CONVERSION
# string to integer
s = "10"
print(int(s) + 5)
# string to float 
f = float("7.9")
print(f)

# integer to string
n = 5
print("The number is " + str(n))

# float to integer
pi = 3.14
print(int(pi))

# integer to boolean
print(bool(1))

# false to boolean
print(bool("False"))  # Non-empty string returns True

# int to string * by 2
num = int(input("Enter a number: "))
print(num * 2)
# float to integer and printing both the origional and converted values
f = float(input("Enter a float: "))
print("Original:", f, "Converted:", int(f))
# convert a string and check type
x = 123
x_str = str(x)
print("Type:", type(x_str))
# two numbes from user and add as integers
a = int(input("Enter a number: "))
b = int(input("Enter another: "))
print("Sum:", a + b)
# string input to float and int
s = "25.5"
print("Float:", float(s), "Int:", int(float(s)))


# take a string input and then convert to int if it is
s = input("Enter a string: ")
if s.isnumeric():
    print(int(s))
else:
    print("Not numeric.")


# Convert a float to int and then to stringf = 9.99
i = int(f)
s = str(i)
print(f"Float: {f}, Int: {i}, String: {s}")
