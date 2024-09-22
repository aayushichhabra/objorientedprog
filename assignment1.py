#q1
a=int(input("Q1-enter a number:"))
if a%2==0:
    print("even number")
else:
    print("odd number")

print("\n")


#q2
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


x=int(input("Q2-enter a number:"))
print(factorial(x))

print("\n")


#q3
def factors(n):
    factorlist=[]
    for i in range (1,n+1):
        if n%i==0:
            factorlist=factorlist+[i]
    return (factorlist)


def isprime(n):
    return (factors(n)==[1,n])

def primesupton(n):
    plist=[]
    for i in range(1,n+1):
        if isprime(i)==True:
            plist=plist+[i]
    return(plist)

print("Q3-all prime nos smaller than 100:",primesupton(100))

print("\n")


#q4
def count_characters(s):
    char_count = {}  
    for char in s:
        if char in char_count:
            char_count[char] += 1 
        else:
            char_count[char] = 1   
    return char_count
str1=input("Q4-enter a string:")
print(count_characters(str1))

print("\n")

#q5
birthdays = {
    "Alice": "1990-04-12",
    "Bob": "1988-06-23",
    "Charlie": "1995-11-05"
}
name = input("Q5-Enter the name to find the birthday: ").strip()
if name in birthdays:
    birthday = birthdays[name]
    print(f"{name}'s birthday is: {birthday}")
    birthday_parts = birthday.split("-")
    year, month, day = birthday_parts[0], birthday_parts[1], birthday_parts[2]
    print(f"Year: {year}, Month: {month}, Day: {day}")
    formatted_birthday = "/".join([month, day, year])
    print(f"Formatted Birthday: {formatted_birthday}")
else:
    print("Name not found in the dictionary.")

print("\n")


#q6
import statistics
numbers = [4, 2, 7, 8, 2, 3, 9, 10, 4, 2]
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)
print(f"Q6-Numbers: {numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")


print("\n")

#q7
def dups(lst):
    seen = set()
    duplicates = set()
    for elem in lst:
        if elem in seen:
            duplicates.add(elem)
        else:
            seen.add(elem)
    return list(duplicates)
numbers = [1, 3, 5, 3, 7, 9, 1, 3, 5, 7]
duplicate_elements = dups(numbers)

print(f"Q7-List of duplicate elements: {duplicate_elements}")

print("\n")

#q8
def add_matrices(matrix1, matrix2):
    n = len(matrix1)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result
matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]
result_matrix = add_matrices(matrix1, matrix2)
print("Q8-Result of matrix addition:")
for row in result_matrix:
    print(row)

print("\n")


#q9
def multiply_matrices(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])
    if cols_matrix1 != rows_matrix2:
        raise ValueError("Number of columns in matrix1 must be equal to number of rows in matrix2.")
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]
result_matrix = multiply_matrices(matrix1, matrix2)
print("Q9-Result of matrix multiplication:")
for row in result_matrix:
    print(row)

print("\n")

#q10
def is_valid_parentheses(s):
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
print("Q10- valid parenthesis")
print(is_valid_parentheses("()"))          
print(is_valid_parentheses("()[]{}"))      
print(is_valid_parentheses("(]"))         
print(is_valid_parentheses("([)]"))        
print(is_valid_parentheses("{[]}"))        
print(is_valid_parentheses("{{{"))

print("\n")        

#q11
def subsets(nums):
    result = []
    def backtrack(start, current_subset):
        result.append(current_subset[:])
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
    backtrack(0, [])
    return result
nums = [1, 2, 3]
unique_subsets = subsets(nums)
print("Q11-All unique subsets:")
for subset in unique_subsets:
    print(subset)




