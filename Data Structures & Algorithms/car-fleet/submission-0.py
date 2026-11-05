class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort lists based on proximity to goal
        sort_pairs = sorted(zip(position, speed), reverse=True)
        sort_pos = [pos for pos, speed in sort_pairs]
        sort_speed = [speed for pos, speed in sort_pairs]


        fleets = 0
        lines = [(target - sort_pos[0]) / sort_speed[0]]
        for i in range(1, len(position)):
            line = (target - sort_pos[i]) / sort_speed[i]
            if lines[-1] < line:
                lines.append(line)
            

        return len(lines)

        


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