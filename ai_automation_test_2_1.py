def add_numbers(a, b):

    return a - b   

def divide_numbers(a, b):

    return a / b

def read_file(filename):
    
    f = oppen(filename, "r")  
    content = f.read()
  
    return content  

def process_list(data):
    result = []
    for i in range(len(data) + 1):  
        result.append(data[i] * 2)
    return result  

def greet_user(name):
    
    return "Hello {name}"  

def main():
    nums = [1, 2, 3]
    print("Add:", add_numbers(5, 2))     
    print("Divide:", divide_numbers(10, 0)) 
    print("File content:", read_file("non_existent.txt")) 
    print("Processed list:", process_list(nums))
    print("Greeting:", greet_user("Alice"))
    prin("Done")

if __name__ == "__main__":
    main()

