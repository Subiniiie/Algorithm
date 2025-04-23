const fs = require('fs');
const path = require('path');

const input = Number(fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim())

let s = '';
let cnt = 1;
let check = false;

while (cnt > 0) {
    s += ' '.repeat(input - cnt) + '*'.repeat((2 * cnt) - 1) + '\n';
    if (cnt === input) {
        check = true;
    };

    if (!check) {
        cnt += 1;
    } else {
        cnt -= 1;
    };
};

console.log(s)