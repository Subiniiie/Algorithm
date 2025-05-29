const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim()

const N = Number(input);

let answer = '';

if (N % 2 === 1) {
    answer = 'SK'
} else {
    answer = 'CY'
};

console.log(answer)
