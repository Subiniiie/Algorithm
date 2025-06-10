const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.trim().split(" ").map(Number));

const N = input[0][0];
let A = input[1];
let B = input[2];

let answer = 0;

A.sort(function(a, b) {
    if (a > b) return 1;
    if (a === b) return 0;
    if (a < b) return -1;
});

B.sort(function(a, b) {
    if (a > b) return -1;
    if (a === b) return 0;
    if (a < b) return 1;
});

for (let i = 0; i < N; i++) {
    answer += (A[i] * B[i]);
};

console.log(answer)