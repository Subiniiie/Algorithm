const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.split(" ").map(Number));

let t = input[1][0];
let s = 0;

for (let i = 2; i < 2 + t; i++) {
    s += input[i][0] * input[i][1];
};

if (s === input[0][0]) {
    console.log('Yes');
} else {
    console.log('No');
};