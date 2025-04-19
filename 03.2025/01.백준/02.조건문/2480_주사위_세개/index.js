const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split(" ").map(Number);

const A = input[0];
const B = input[1];
const C = input[2];

if (A === B) {
    if (A === C) {
        console.log(10000 + A * 1000);
    } else {
        console.log(1000 + A * 100);
    }
} else {
    if (A === C) {
        console.log(1000 + A * 100);
    } else {
        if (B === C) {
            console.log(1000 + B * 100);
        } else {
            console.log(Math.max.apply(null, input) * 100);
        }
    }
} 