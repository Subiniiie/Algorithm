const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().split(" ").map(Number);

const A = input[0];
const B = input[1];

if (A > B) {
    console.log('>');
} else if (A < B) {
    console.log('<');
} else {
    console.log('==');
};