
def funct(array, pointer=0, sum=0):
    if pointer < len(array):
        sum += funct(array, pointer+1, array[pointer])
    return sum

arr = [1,2,3,4,5,6,7,8]
print(funct(arr))


