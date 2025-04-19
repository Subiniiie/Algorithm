const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.split(" ").map(Number));

let answer = '';
let i = 0;

while (i >= 0) {
    const a = input[i][0];
    const b = input[i][1];
    if (a === 0 && b === 0) {
        break;
    } else {
        answer += (a + b) + '\n'
    };
    i++;
};

console.log(answer)