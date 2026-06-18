class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict={}
        
        #the frequency of a num cannot be larger than the len of nums
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq_dict.items():  
            #each bucket represents a frequency, add the number to the equivalent bucket index, based on count 
            buckets[count].append(num)
        
        out = []
        for i in range(len(buckets)-1, 0, -1):
            if buckets[i]:
                out += buckets[i] 
            if len(out) >= k:
                return out[:k]
        



    '''
    
    '''
