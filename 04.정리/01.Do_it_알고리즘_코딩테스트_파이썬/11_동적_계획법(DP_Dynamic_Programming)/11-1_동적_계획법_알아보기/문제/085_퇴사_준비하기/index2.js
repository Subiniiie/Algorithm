// 백준 14501

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(Number))

const N = input[0][0];
let D = new Array(N+2).fill(0);

let T = new Array(N+1).fill(0);
let P = new Array(N+1).fill(0);

for (let i = 1; i <= N; i++) {
    T[i] = input[i][0];
    P[i] = input[i][1];
};

for (let i = N; i >= 0; i--) {
    if (i + T[i] > N+1) {
        D[i] = D[i+1]
    } else {
        D[i] = Math.max(D[i+1], P[i] + D[i+T[i]])
    };
};

console.log(D[1])