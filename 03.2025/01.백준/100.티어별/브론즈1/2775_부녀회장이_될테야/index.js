const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map(Number);


const T = input[0];
let D = Array.from(Array(15), () => Array(15).fill(0));

let answer = '';

for (let i = 1; i <= 14; i++) {
    D[0][i] = i;
};

for (let i = 1; i <= 14; i++) {
    for (let j = 1; j <= 14; j++) {
        if (j === 1) {
            D[i][j] = 1;
        } else {
            D[i][j] = D[i-1][j] + D[i][j-1]
        };
    };
};

for (let i = 1; i < input.length; i += 2) {
    answer += (D[input[i]][input[i+1]] + '\n')
};

console.log(answer)