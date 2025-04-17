const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    "/dev/stdin" : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map(Number);

const A = input[0];
const B = input[1];
const [x, y, z] = String(B).split('').map(Number);

console.log(A * z);
console.log(A * y);
console.log(A * x);
console.log(A * B);