const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, "input.txt")
).toString().split("\n").map((el) => el.split(" ").map(Number));


const [N, M, R] = input[0];
let graph = Array.from({ length: N + 1 }, () => []);

for (let i = 1; i < M + 1; i++) {
    const [u, v] = input[i];
    graph[u].push(v);
    graph[v].push(u);
};

graph.forEach(adj => adj.sort((a, b) => a - b));

const DFS = (g, startNode) => {
    let visited = [];
    let stack = [startNode];

    while (stack.length) {
        const node = stack.pop();
        if (visited.includes(node)) continue;

        visited.push(node);

        for (let i = g[node].length - 1; i >= 0; i--) {
            const next = g[node][i];
            if(!visited.includes(next)) stack.push(next);
        }
    }

    return visited;
};

const order = DFS(graph, R);
console.log(order.join("\n"))