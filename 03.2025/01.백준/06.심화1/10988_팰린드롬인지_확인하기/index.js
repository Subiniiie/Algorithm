const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim()

const c = Math.floor(input.length / 2);
const t = input.length - 1;
let i = 0;

while (true) {
    if (input[i] === input[t - i]) {
        i += 1;
        if (i > c) {
            console.log(1);
            break;
        };
    } else {
        console.log(0);
        break
    };
};