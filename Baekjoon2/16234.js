const input = require("fs")
  .readFileSync("./example.txt")
  .toString()
  .trim()
  .split("\n");

const [N, L, R] = input[0].split(" ").map(Number);

const countries = [];

for (let i = 1; i <= N; i++) {
  countries.push(input[i].split(" ").map(Number));
}

const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

function bfs(countries, visited, start) {
  const [sx, sy] = start;

  const result = [];
  if (visited[sx][sy]) {
    return result;
  }
  visited[sx][sy] = true;

  const queue = [[sx, sy]];

  result.push([sx, sy]);

  while (queue.length > 0) {
    const [cx, cy] = queue.shift();

    for (let i = 0; i < 4; i++) {
      const nx = cx + dx[i];
      const ny = cy + dy[i];

      if (
        nx >= 0 &&
        nx < N &&
        ny >= 0 &&
        ny < N &&
        !visited[nx][ny] &&
        L <= Math.abs(countries[cx][cy] - countries[nx][ny]) &&
        Math.abs(countries[cx][cy] - countries[nx][ny]) <= R
      ) {
        visited[nx][ny] = true;
        result.push([nx, ny]);
        queue.push([nx, ny]);
      }
    }
  }

  return result;
}

let people = 0;

while (true) {
  const visited = Array.from({ length: N }, () => Array(N).fill(false));
  const targets = [];

  for (let x = 0; x < N; x++) {
    for (let y = 0; y < N; y++) {
      const result = bfs(countries, visited, [x, y]);
      if (result.length > 1) {
        targets.push(result);
      }
    }
  }

  if (targets.length === 0) {
    break;
  }

  for (const sumTargets of targets) {
    const average = Math.floor(
      sumTargets.reduce((acc, [x, y]) => acc + countries[x][y], 0) /
        sumTargets.length
    );

    for (const [x, y] of sumTargets) {
      countries[x][y] = average;
    }
  }

  people++;
}

console.log(people);
