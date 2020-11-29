from typing import List

class Solution:
    def __init__(self):
        self.all_paths = list()
        self.graph = list()
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.dfs(0, len(self.graph)-1, [0])
        return self.all_paths
    def dfs(self, vertex, stop_vertex, visited_vertices):
        if vertex == stop_vertex:
            self.all_paths.append(visited_vertices)
            return
        for neighbour in self.graph[vertex]:
            self.dfs(neighbour, stop_vertex, visited_vertices+[neighbour])
        

if __name__ == "__main__":
    input_list = [
        [[1,2],[3],[3],[]],
        [[4,3,1],[3,2,4],[3],[4],[]],
        [[1],[]],
        [[1,2,3],[2],[3],[]],
        [[1,3],[2],[3],[]]
    ]
    for input_item in input_list:
        print("\ninput=", input_item)
        output = Solution().allPathsSourceTarget(input_item)
        print("output=", output)