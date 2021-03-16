
def funct(array, pointer=0, dict={}):
    if pointer < len(array):
        if array[pointer][0] not in dict.keys():
            dict[array[pointer][0]] = len(array[pointer])
        else:
            if dict.get(array[pointer][0]) < len(array[pointer]):
                dict[array[pointer][0]] = len(array[pointer])
        funct(array, pointer+1, dict)
    return [[k,v] for k,v in dict.items()]

arr = ['aa', 'aaaaaaa', 'b', 'b', 'bbbbbb', 'cccc', 'c']
print(funct(arr))