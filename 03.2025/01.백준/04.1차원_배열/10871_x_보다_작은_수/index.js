const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.split(" ").map(Number));

const N = input[0][0];
const X = input[0][1];

let a = '';

for (let i = 0; i < N; i++) {
    const temp = input[1][i];
    if (temp < X) {
        a += temp + " "
    };
};

console.log(a)