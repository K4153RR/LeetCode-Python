class Answer(object):
'''80. Remove Duplicates from Sorted Array II'''
    def removeDuplicates(nums):
        i = 0
        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1
        return i