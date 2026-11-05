class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort lists based on proximity to goal
        sort_pairs = sorted(zip(position, speed), reverse=True)

        lines = (target - sort_pairs[0][0]) / sort_pairs[0][1]
        count = 1
        for i in range(1, len(position)):
            pair = sort_pairs[i]
            line = (target - pair[0]) / pair[1]
            if lines < line:
                count += 1
                lines = line
        return count

        


        '''
t = 10
pos = [1,4] 
spe = [3,2]

10 = 3x + 1
x = 3

10 = 2x + 4
x = 3

meetup at 10, fleet = 1

t = 10
pos = [4,1,0,7]
spe = [2,2,1,1]

10 = 2x + 4
x = 3

10 = 2x + 1
x = 4.5

10 = 1x + 0
x = 10

10 = 1x + 7
x = 3

pos 4 and 7 intersect at 10, the other cars never intersect so there are 3 fleets

        '''