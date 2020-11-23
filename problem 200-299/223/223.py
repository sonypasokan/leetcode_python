"""
2 cases possible
1. the intervals dont intersect, hence just add the sum of areas
2. the intervals do intersect, hence the intersecting x and y needs to be found out. Then this value has to be subtracted from the total area.

In any case the first step is to find the area.
then check if intervals have intersection or not.
then get the length and width of intersecting rectangle.

"""

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area_1 = self.__compute_area(A, B, C, D)
        area_2 = self.__compute_area(E, F, G, H)
        if area_1 == 0:
            return area_2
        elif area_2 == 0:
            return area_1
        area_intersection = self.__compute_intersection_area(A, B, C, D, E, F, G, H)
        return area_1 + area_2 - area_intersection
        
    def __compute_area(self, x1, y1, x2, y2):
        return (x2 - x1) * (y2 - y1)
    
    def __compute_intersection_area(self, x1, y1, x2, y2, x3, y3, x4, y4):
        if x1 < x3:
            first_x_pair = (x1, x2)
            second_x_pair = (x3, x4)
        else:
            first_x_pair = (x3, x4)
            second_x_pair = (x1, x2)
        if y1 < y3:
            first_y_pair = (y1, y2)
            second_y_pair = (y3, y4)
        else:
            first_y_pair = (y3, y4)
            second_y_pair = (y1, y2)
            
        if first_x_pair[1] > second_x_pair[0]: # overlapping x value
            diff_x = abs(second_x_pair[0] - min(first_x_pair[1], second_x_pair[1]))
        else:
            diff_x = 0
        if first_y_pair[1] > second_y_pair[0]: # overlapping y value
            diff_y = abs(second_y_pair[0] - min(first_y_pair[1], second_y_pair[1]))
        else:
            diff_y = 0
        return diff_x * diff_y
        
if __name__ == "__main__":
    input_list = [
        [-3, 0, 3, 4, 0, -1, 9, 2],
        [0, 0,0,0,-1,-1,1,1],
        [-2,-2,2,2,3,3,4,4],
        [-2,-2,2,2,-1,-1,1,1]
    ]
    for input_item in input_list:
        print("input=", input_item)
        output = Solution().computeArea(*input_item)
        print("output=", output)
        