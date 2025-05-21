class Solution:
    def twoSum(self, nums=[2,7,11,15], target=9) :
        map={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in map:
                return [map[diff],i]
            map[n]=i
        return

if __name__ == '__main__':
    s=Solution()
    twoSum=s.twoSum()
    print(twoSum)