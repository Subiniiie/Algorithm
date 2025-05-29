const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(' ').map(Number))

const N = input[0][0];
let T = new Array(N+1).fill(0);
let P = new Array(N+1).fill(0);

let D = new Array(N+2).fill(0);

for (let i = 1; i < N+1; i++) {
    const [t, p] = input[i];
    T[i] = t;
    P[i] = p;
};

for (let i = N; i > 0; i--) {
    if (i + T[i] > N + 1) {
        D[i] = D[i+1];
    } else {
        D[i] = Math.max(D[i+1], D[i+T[i]] + P[i]);
    }
};

console.log(D[1])