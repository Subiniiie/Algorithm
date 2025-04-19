const fs = require('fs');
const path = require('path');

const input = +fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

let s = 0;

for (let i = 1; i < input + 1; i++) {
    s += i;
};

console.log(s)