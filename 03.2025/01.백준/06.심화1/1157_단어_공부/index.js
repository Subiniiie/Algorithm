const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim()

const alpha = {
    'A' : 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
    'F' : 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
    'K' : 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    'P' : 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,
    'U' : 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0,
};

for (const element of input) {
    const t = element.toUpperCase();
    alpha[t] += 1;
};

let s = 0;
let c = 0;
let a = '';

for (var key in alpha) {
    if (alpha[key] > s) {
        s = alpha[key]
        a = key;
    } else if (alpha[key] === s) {
        c = alpha[key]
    };
};

if (s === c) {
    a = '?';
};

console.log(a)
