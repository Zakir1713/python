# 1. Print a simple message

print("Hello World")


# 2. Print multiple items in one statement

print("Name: Zakir, Age: 22, City: Nowshera")


# 3. Print using escape characters

print("Welcome to Python!\nLets learn Python")


# 4. Print quotes inside a string

print("He said,\"Python is amazing\"")



# 5. Print a pattern using stars
for i in range(5):
    for j in range(i+1):
        print('*', end=" ")
    print()       

##########################################################

# Intermediate Output Exercise

# Formate string output using f-string

name = "Zakir"
age = "22"
print(f"Hello, My name is: {name}, and I am {age} years old")

# Print a table
for i in range (1, 11):
    print("5","X",i, "=",i*5)


# Text with Padding

print(f"{'apple':>10}{'Banana':>10}{'cherry':>10}")


#simple calculation result output

print(f"5 + 7 ={5+7}")

#print formatted recipt

print("Item Name    Quantity    Price")
print("Eggs         6           180")
print("Banana       12          160")
print("Total:                   340")