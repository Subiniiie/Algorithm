// 백준 1463

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

const N = Number(input);
let D = new Array(N+1).fill(0);


for (let i = 2; i <= N; i++) {
    D[i] = D[i-1] + 1;
    if (i % 2 === 0) {
        D[i] = Math.min(D[i], D[i/2] + 1);
    };
    if (i % 3 === 0) {
        D[i] = Math.min(D[i], D[i/3] + 1);
    };
};

console.log(D[N])