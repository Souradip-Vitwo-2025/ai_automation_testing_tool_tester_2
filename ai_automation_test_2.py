def add_numbers(a, b):
    # Fixed: correct operator
    return a + b   

def divide_numbers(a, b):
    # Fixed: handle division by zero
    if b == 0:
        return "Error: Division by zero"
    return a / b

def read_file(filename):
    # Fixed: correct function name and ensure file is closed
    try:
        with open(filename, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "Error: File not found"

def process_list(data):
    result = []
    # Fixed: correct loop range
    for i in range(len(data)):
        result.append(data[i] * 2)
    return result  

def greet_user(name):
    # Fixed: use f-string
    return f"Hello {name}"  

def main():
    nums = [1, 2, 3]
    print("Add:", add_numbers(5, 2))     # should be 7
    print("Divide:", divide_numbers(10, 0))  
    print("File content:", read_file("non_existent.txt"))  
    print("Processed list:", process_list(nums))
    print("Greeting:", greet_user("Alice"))
    print("Done")  # Fixed typo

if __name__ == "__main__":
    main()
