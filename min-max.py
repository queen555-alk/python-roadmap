#using built in functions
def minMax(arr):
    smallest = min(arr)
    largest = max(arr)
    return smallest, largest

def main():
    arr1 = [1,4,2,9,4,5]
    print(minMax(arr1))

main()