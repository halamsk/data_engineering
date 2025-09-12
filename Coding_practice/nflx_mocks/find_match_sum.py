#Chatpgt
# Problem (core):
# You’re given an array of positive integers nums and a target integer S. Return the minimum length of a contiguous subarray whose sum is ≥ S. If none exists, return 0.

# Examples

# nums = [2,3,1,2,4,3], S = 7 → answer 2 (subarray [4,3])

# nums = [1,1,1,1], S = 5 → 0

# Constraints (baseline):

# 1 ≤ len(nums) ≤ 1e5

# 1 ≤ nums[i] ≤ 1e9

# Time focus: near O(n). Space O(1) preferred.

def find_min_match_sum_len(arr,s):
    if len(arr)<=1:
       return True if sum(arr)==s else False
    start,end = 0,0
    current_sum = 0
    min_len = 0
    while end<len(arr):
        current_sum += arr[end]
        # print(start)
        # print(end)
        # print(current_sum)
        # print("##################")
        if current_sum<s:
            end += 1
        else:
            if current_sum == s:
               min_len = min(min_len, end-start+1)
            current_sum -= arr[start]
            start += 1
            end += 1

    return min_len

nums = [2,3,1,2,4,3]
S = 7
print(find_min_match_sum_len(nums,S))
    

