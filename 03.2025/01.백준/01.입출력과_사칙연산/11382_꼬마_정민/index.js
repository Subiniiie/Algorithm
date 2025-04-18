const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split(" ").map(Number);

const A = input[0];
const B = input[1];
const C = input[2];

console.log(A + B + C);