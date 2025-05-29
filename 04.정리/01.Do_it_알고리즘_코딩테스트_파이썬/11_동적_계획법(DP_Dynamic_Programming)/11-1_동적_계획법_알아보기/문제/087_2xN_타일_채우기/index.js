// 백준 11726

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

const N = Number(input);
let D = new Array(N + 1);

D[1] = 1;

if (N >= 2) {
    D[2] = 2;
};

for (let i = 3; i <= N; i++) {
    D[i] = (D[i-2] + D[i-1]) % 10007
};

console.log(D[N])