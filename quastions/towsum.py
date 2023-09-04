
list_0f_io = [{"input": [[2,7,11,15], 9], "output": [0,1]}, {"input": [[3,2,4], 6], "output": [1,2]}, {"input": [[3,3], 6], "output": [0,1]},{"input":[ [10, 20, 30, 40], 50], "output":[1, 2]}]
def tow_sum(numbers =[2,7,11,15], target=9):
    fict_of_nums = {}
    for i in range(len(numbers)):
        fict_of_nums[numbers[i]] = i
    for i in range(len(numbers)):
        if target - numbers[i] in fict_of_nums and fict_of_nums[target - numbers[i]] != i:
            return [i, fict_of_nums[target - numbers[i]]]
    return None


print(tow_sum())