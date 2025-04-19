const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.split(" ").map(Number));

const t = input.length;
let a = '';

for (let i = 0; i < t; i++) {
    a += (input[i][0] + input[i][1]) + '\n'
};

console.log(a)