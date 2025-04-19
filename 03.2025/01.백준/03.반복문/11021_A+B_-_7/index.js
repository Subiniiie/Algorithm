const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux'?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.split(" ").map(Number));

let a = '';
const t = input[0][0];

for (let i = 1; i < t + 1; i++) {
    a += "Case #" + i + ": " + (input[i][0] + input[i][1]) + '\n';
};

console.log(a)