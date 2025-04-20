const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map(line => line.trim());

const T = Number(input[0]);

let a = '';

for (let i = 1; i < T + 1; i++) {
    let temp = '';
    const s = input[i];
    temp += s[0] + s[s.length - 1];
    if (i === T) {
        a += temp;
    } else {
        a += temp + "\n";
    };
};

console.log(a)