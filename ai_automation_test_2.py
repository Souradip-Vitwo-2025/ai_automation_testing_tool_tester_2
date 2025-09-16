def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def process_items(items):
    result = []
    for i in range(len(items)):
        result.append(items[i] * 2)
    return result

def stringify(nums):
    return "-".join(map(str, nums))

def main():
    nums = [1, 2, 3]
    total = add(nums[0], nums[1])
    print("Total:", total)
    print("Division:", divide(10, 0))
    print("Processed:", process_items(nums))
    print("Stringified:", stringify(nums))
    print("Done")

if __name__ == "__main__":
    main()