const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.split(' ').map(Number));

const N = input[0][0];
const M = input[0][1];

let arr = [...new Array(N)].map((_, i) => i + 1);

let a = '';


for (let i = 1; i < M + 1; i++) {
    [arr[input[i][0] - 1], arr[input[i][1] - 1]] = [arr[input[i][1] - 1], arr[input[i][0] - 1]]
};

for (let i = 0; i < N; i++) {
    if (i === N - 1) {
        a += arr[i]
    } else {
        a += arr[i] + " "
    };
};

console.log(a)