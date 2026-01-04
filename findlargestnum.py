import os

#clear the console
os.system('cls' if os.name == 'nt' else 'clear')

def find_largest_loop(numbers_list):
    """
    This functions finds the largest number in a array.
    """
    if not numbers_list:
        return None
    
    largest_num = numbers_list[0] # Assume the first element is the largest initially

    for num in numbers_list:
        if num > largest_num:
            largest_num = num # Update if a larger number is found

    return largest_num

# Read a list of values from user input and store in a list
values = input("Enter values separated by spaces: ").split()
# Convert to integers if needed (assuming numbers)
my_list = [int(x) for x in values]

largest = find_largest_loop(my_list)
print(f"The largest number is: {largest}")
