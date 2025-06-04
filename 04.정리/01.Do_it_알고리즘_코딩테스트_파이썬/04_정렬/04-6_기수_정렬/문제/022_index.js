// 백준 10989

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '022_input.txt')
).toString().trim().split("\n").map((el) => el.trim()).map(Number);

let D = new Array(10001).fill(0);
const N = input[0];

for (let i = 1; i <= N; i++) {
    D[input[i]] += 1;
};

let answer = "";

for (let i = 1; i < 10001; i++) {
    if (D[i] !== 0) {
        answer += i + '\n';
    };
};

console.log(answer)