#using built in functions
def minMax(arr):
    smallest = min(arr)
    largest = max(arr)
    return smallest, largest

def minMax2(arr):
    smallest = arr[0]
    largest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
        elif i > largest:
            largest = i
    return smallest, largest

def main():
    arr1 = [1,4,2,9,4,5]
    print(minMax(arr1))
    print(minMax2(arr1))

main()