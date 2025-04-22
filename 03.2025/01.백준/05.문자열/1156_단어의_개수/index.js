const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split(' ');

let cnt = 0;

if (input.includes('')) {
    cnt = 0;
} else {
    cnt = input.length;
};

console.log(cnt)
