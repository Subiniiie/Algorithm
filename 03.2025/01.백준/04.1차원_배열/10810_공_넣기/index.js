const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.split(' ').map(Number));

const N = input[0][0];
const M = input[0][1];

let arr = new Array(N).fill(0);

let answer = '';


for (let q = 1; q < M + 1; q++) {
    const i = input[q][0];
    const j = input[q][1];
    const k = input[q][2];
    for (let r = i; r < j + 1; r++) {
        arr[r - 1] = k;
    };
};

for (let i = 0; i < N; i++) {
    if (i === N - 1) {
        answer += arr[i]
    } else {
        answer += arr[i] + ' '
    };
};

console.log(answer)