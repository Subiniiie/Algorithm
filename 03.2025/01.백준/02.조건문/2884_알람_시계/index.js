const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split(' ').map(Number);

let H = input[0];
let M = input[1];

if (M >= 45) {
    M -= 45
    console.log(H+" "+M);
} else {
    if (H === 0) {
        H = 23
    } else {
        H -= 1
    }
    M += 15
    console.log(H+" "+M)
};

