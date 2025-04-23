const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.trim())

let s = '';

for (let i = 0; i < input.length ; i++) {
    if (i === input.length - 1) {
        s += input[i];
    } else {
        s += input[i] + '\n';
    };
};

console.log(s)