function solution(n, s, a, b, fares) {
  var answer = 0;
  const nodes = Array.from({length : n}, ()=> Array.from({length : n }, ()=> Infinity));
  
  
  
  for (const [start,end,cost] of fares){
      nodes[start - 1][end - 1] = cost;
      nodes[end - 1][start - 1] = cost;
  }

  
  const aDistances = Array.from({length : n } , () => Infinity);
  const bDistances = Array.from({length : n }, () => Infinity);
  const sDistances = Array.from({length : n }, () => Infinity);
  
  function findSmallestNode (visited, distances){
      let minDist = Infinity;
      let minIdx = 0;
      
      for(let i  = 0; i < distances.length ; i++){
          if(visited[i]) continue;
          if(distances[i] < minDist){
              minDist = distances[i];
              minIdx = i;
          }
      }
      return minIdx;
  }
  
  function dijkstra(distances, start){
      const visited = Array.from({length : n }, ()=> false);
      distances[start] = 0;
      
      for(let i = 0; i < distances.length ; i++){
          const nodeIdx = findSmallestNode(visited, distances);
          visited[nodeIdx] = true;

          
          for(let j = 0; j < distances.length; j++){
              if (!visited[j] && nodes[nodeIdx][j] !== Infinity) {
                  if (distances[j] > distances[nodeIdx] + nodes[nodeIdx][j]) {
                      distances[j] = distances[nodeIdx] + nodes[nodeIdx][j];
                  }
              }
          }
      }
  }
  
  dijkstra(aDistances, a - 1);
  dijkstra(sDistances, s - 1);
  dijkstra(bDistances, b - 1);
  
  return answer;
}
