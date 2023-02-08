def has_33(nums):
    is_true = "false"
    for i in range(len(nums)):
        if nums[i] == 3:
            for t in range(i + 1,len(nums)):
                if nums[t] == 3:
                    is_true = "true"
                    break
                else:
                    break
    return is_true
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3])) 
                    