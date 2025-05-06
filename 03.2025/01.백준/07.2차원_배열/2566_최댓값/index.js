const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.trim().split(" ").map(Number))

let n = 0;
let p = '1 1';

for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
        const temp = input[i][j];
        if (n < temp) {
            n = temp;
            p = (i + 1) + ' ' + (j + 1);
        };
    };
};

console.log(n)
console.log(p)