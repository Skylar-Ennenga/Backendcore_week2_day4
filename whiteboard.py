# Find Even numbers

# Create a function that, given a list as a parameter, finds the even numbers inside the list. The function should then return a list.
# Example:
# Input: [2, 7, 10, 11, 12]
# Output: [2, 10, 12]

numbers = [2, 7, 10, 11, 12]

def even_numbers(number):
    even = []
    for x in number:
        if x % 2 == 0:
            even.append(x)
    
    return even
            
          
even_numbers(numbers)

print(even_numbers(numbers))