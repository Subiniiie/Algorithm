const fs = require('fs');
const path = require('path');

const input = +fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

let a = '';

for (let i = 0; i < input; i++) {
    a += "*".repeat(i+1) + '\n'
};

console.log(a)