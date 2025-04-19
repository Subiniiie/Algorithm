const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map(Number);

let arr = new Array(30).fill(0);

for (const element of input) {
    arr[element - 1] = element;
};

let minNum = 30;
let maxNum = 1;

for (let i = 0; i < 30; i++) {
    const temp = arr[i];
    if (temp === 0) {
        if (minNum > i + 1) {
            minNum = i + 1;
        } else if (maxNum < i + 1) {
            maxNum = i + 1;
        }
    };
};

console.log(minNum + '\n' + maxNum)