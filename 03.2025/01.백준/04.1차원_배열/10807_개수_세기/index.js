const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.split(" ").map(Number));

let cnt = 0;

for (let i = 0; i < input[0][0]; i++) {
    if (input[1][i] === input[2][0]) {
        cnt += 1;
    };
};

console.log(cnt)