class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0
            freq_dict[num] += 1

        sorted_list = sorted(freq_dict.items(), key= lambda item:item[1], reverse=True)
        out = []
        #for i in range(k):
        #    out.append(sorted_list[i][0])
        return  [num for num, count in sorted_list[:k]]
        



    '''
    
    '''
