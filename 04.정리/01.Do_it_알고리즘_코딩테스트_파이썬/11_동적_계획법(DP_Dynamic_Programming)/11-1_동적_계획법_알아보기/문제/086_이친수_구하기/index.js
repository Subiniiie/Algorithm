// 백준 2193

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim()

const N = Number(input);
let D = new Array(N+1).fill(0n);

D[1] = 1n;

if (N >= 2) {
    D[2] = 1n;
};

for (let i = 3; i <= N; i++) {
    D[i] = D[i-1] + D[i-2];
};

console.log(D[N].toString())