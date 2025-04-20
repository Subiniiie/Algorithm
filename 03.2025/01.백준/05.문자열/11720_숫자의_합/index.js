const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((line) => line.trim())

const t = Number(input[0]);
const arr = input[1];
const r = input[1].length;

let a = 0;

for (let i = 0; i < r; i++) {
    a += Number(arr[i]);
};

console.log(a)