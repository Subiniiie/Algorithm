const fs = require('fs');
const path = require('path');

const input = +fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

let a = '';

for (let i = 1; i < input + 1; i++) {
    a += " ".repeat(input - i) + "*".repeat(i) + '\n'
};

console.log(a)