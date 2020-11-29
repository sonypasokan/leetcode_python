from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        people_graph = {person:set() for person in range(1, N+1)}
        for from_person, to_person in trust:
            people_graph[from_person].add(to_person)
        
        possible_judges = {person for person in people_graph if people_graph[person]==set()}

        for judge in possible_judges:
            is_judge = True
            for person in people_graph:
                if person == judge:
                    continue
                if not judge in people_graph[person]:
                    is_judge = False
                    break
            if is_judge == True:
                return judge
        return -1

if __name__ == "__main__":
    input_list = [
        [2, [[1,2]]],
        [3, [[1,3],[2,3]]],
        [3, [[1,3],[2,3],[3,1]]],
        [3, [[1,2],[2,3]]],
        [4, [[1,3],[1,4],[2,3],[2,4],[4,3]]]
    ]
    for input_item in input_list:
        print("\ninput=", input_item)
        output = Solution().findJudge(input_item[0], input_item[1])
        print("output=", output)
