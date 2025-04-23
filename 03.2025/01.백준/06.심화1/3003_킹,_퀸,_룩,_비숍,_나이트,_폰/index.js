const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform == 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split(' ').map(Number)

let p = [1, 1, 2, 2, 2, 8];
let s = '';

for (let i = 0; i < 6; i++) {
    let t = p[i] - input[i];
    if (i === 5) {
        s += t;
    } else {
        s += t += ' ';
    };
};

console.log(s)