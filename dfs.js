function dfs(graph, index, visited) {
  visited[index] = true;
  console.log(index);
  for (let node of graph[index]) {
    if (!visited[node]) dfs(graph, node, visited);
  }
}

const graph = [[1, 2, 4], [0, 5], [0, 5], [4], [0, 3], [1, 2]];
const visited = Array(7).fill(false);

dfs(graph, 0, visited);
