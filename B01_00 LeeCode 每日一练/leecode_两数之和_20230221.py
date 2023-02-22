"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 
的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
"""
# class Solution(object):
def twoSum(self,nums,target):
    for i in range(len(nums)):
        # 计算需要找到的下一个目标数字
        res = target - nums[i]
        # 遍历剩下的元素，查找是否存在该数字
        if res in nums[i+1:]:
            return [i, nums[i+1:].index(res)+i+1]
            # 1,nums[i+1:]是[3,5,7,8]，然后res=7，[3,5,7,8].index(7)是2，在加1+1=4


nums = [1,3,5,7,8]
target = 8
t = twoSum(nums,target)
print(t)