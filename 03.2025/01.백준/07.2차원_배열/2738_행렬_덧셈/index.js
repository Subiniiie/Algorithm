const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map((X) => +X));

const [N, M] = input[0];

const A = [];
const B = [];

let s = '';

for (let i = 1; i < N + 1; i++) {
    A.push(input[i]);
};

for (let i = 1 + N; i < 2 * N + 1; i++) {
    B.push(input[i]);
};

for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
        s += A[i][j] + B[i][j];
        if (j === M - 1) {
            s += '\n'
        } else {
            s += ' '
        };
    };
};

console.log(s)