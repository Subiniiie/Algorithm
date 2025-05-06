const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.trim());

let a= '';
const l = input.length;

for (let i = 0; i < l; i++) {
    const t = input[i].length;
    if (t < 15) {
        const s = 15 - t;
        input[i] += ' '.repeat(s);
    };
};

for (let i = 0; i < 15; i++) {
    for (let j = 0; j < l; j++) {
        const t = input[j][i];
        if (t !== ' ') {
            a += t;
        };
    };
};

console.log(a)