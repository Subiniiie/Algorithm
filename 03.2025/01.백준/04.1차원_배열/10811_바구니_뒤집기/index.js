const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.split(" ").map(Number));

const N = input[0][0];
const M = input[0][1];

let arr = [...new Array(N)].map((_, i) => i + 1);

let a = '';

for (let i = 1; i < M + 1; i++) {
    const a = input[i][0];
    const b = input[i][1];
    const t = Math.floor((b - a + 1) / 2);
    for (let j = 0; j < t; j++) {
        [arr[a - 1 + j], arr[b - 1 - j]] = [arr[b - 1 - j], arr[a -1 + j]]
    };
};

for (let i = 0; i < N; i++) {
    if (i === N - 1) {
        a += arr[i]
    } else {
        a += arr[i] + " "
    };
};

console.log(a)