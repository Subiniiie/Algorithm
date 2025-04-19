const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map(Number);

let arr = new Array(10).fill(0);

for (let i = 0; i < 10; i++) {
    arr[i] = input[i] % 42;
};

let result = [...new Set(arr)];

console.log(result.length)