const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    "/dev/stdin" : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map(Number);

let cnt = 1;
let maxNum = 0;
let a = '';

for (let i = 1; i < 10; i++) {
    const temp = input[i-1];
    if (temp > maxNum) {
        cnt = i;
        maxNum = temp;
    };
};

a += maxNum + '\n' + cnt
console.log(a)