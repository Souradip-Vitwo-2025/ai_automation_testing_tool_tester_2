def add_numbers(a, b):
    # Bug 1: wrong operator
    return a - b   

def divide_numbers(a, b):
    # Bug 2: division by zero not handled
    return a / b

def read_file(filename):
    # Bug 3: wrong function name 'oppen'
    f = oppen(filename, "r")  
    content = f.read()
    # Bug 4: file not closed
    return content  

def process_list(data):
    result = []
    for i in range(len(data) + 1):  # Bug 5: index out of range
        result.append(data[i] * 2)
    return result  

def greet_user(name):
    # Bug 6: missing f-string
    return "Hello {name}"  

def main():
    nums = [1, 2, 3]
    print("Add:", add_numbers(5, 2))     # should be 7
    print("Divide:", divide_numbers(10, 0))  # Bug 7: runtime error
    print("File content:", read_file("non_existent.txt"))  # Bug 8: file not found
    print("Processed list:", process_list(nums))
    print("Greeting:", greet_user("Alice"))
    prin("Done")  # Bug 9: typo in 'print'

if __name__ == "__main__":
    main()
