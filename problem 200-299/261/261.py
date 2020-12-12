class Solution:
    def __init__(self):
        self.graph = dict()

    def validTree(self, n, edges):
        # Check if graph is empty
        if n == 0:
            return True

        # Tree will have a minimum of n-1 edges.
        if len(edges) < n-1:
            return False
        
        # Build the graph with given nodes and edges
        for from_node, to_node in edges:
            if from_node in self.graph:
                self.graph[from_node][to_node] = True
            else:
                self.graph[from_node] = {to_node:True}
            if to_node in self.graph:
                self.graph[to_node][from_node] = True
            else:
                self.graph[to_node] = {from_node:True}
            
        # Check if all nodes are present in the graph
        if len(self.graph) != n:
            return False
        
        # Check if any loops present in the graph
        visited_nodes = {0}
        status, visited_nodes = self.check_loop_with_dfs(0, visited_nodes)
        if status == False or len(visited_nodes) != n:
            # Status=False; when the graph has loops
            # len(visited_nodes) != n; when the graph is not connected
            return False
        return True

    
    def check_loop_with_dfs(self, node, visited_nodes):
        for neighbour, is_available in self.graph[node].items():
            if is_available == False:
                continue
            if neighbour in visited_nodes:
                return False, visited_nodes
            visited_nodes.add(neighbour)
            self.graph[node][neighbour] = False
            self.graph[neighbour][node] = False
            status, visited_nodes = self.check_loop_with_dfs(neighbour, visited_nodes)
            if status == False:
                return False, visited_nodes
        return True, visited_nodes

if __name__ == "__main__":
    input_list = [
        [5, []],
        # [5, [[1,2]]],
        [5, [[0,1], [1,3], [2,3], [2,1], [1,4]]],
        [5, [[2,1], [1,0], [3,0],[4,3]]],
        [6, [[0,2],[2,3],[4,5],[6,5]]]
    ]
    for input_item in input_list:
        output = Solution().validTree(input_item[0], input_item[1])
        print("output=", output)

            
