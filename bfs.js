function BFS(graph, start, visited) {
  const queue = [];
  queue.push(start);
  visited[start] = true;

  while (queue.length !== 0) {
    const v = queue.shift();
    console.log({ v, queue });

    for (const node of graph[v]) {
      console.log({ node });
      if (!visited[node]) {
        queue.push(node);
        visited[node] = true;
      }
    }
  }
}

const graph = [[1, 2, 4], [0, 5], [0, 5], [4], [0, 3], [1, 2]];
const visited = Array(6).fill(false);
BFS(graph, 0, visited);
// 0 1 2 4 5 3
