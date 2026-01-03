import os

#clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# User input
num = int(input("Enter a number: "))

# Print the table
print(f"Multiplication table of {num}:")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
