const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.trim().split(" ").map(Number));

const N = input[0][0];
const M = input[0][1];
const arr = input[1];
const sections = new Array();

for (let i = 2; i < 2 + M; i++) {
    sections.push(input[i])
};

let D = new Array(N+1).fill(0);
D[1] = arr[0];

for (let i = 1; i < N; i++) {
    D[i+1] = D[i] + arr[i];
};

let answer = "";

for (let i = 0; i < M; i++) {
    const start = sections[i][0];
    const end = sections[i][1];

    if (start === 1) {
        answer += (D[end] + "\n")
    } else {
        const temp = D[end] - D[start - 1]
        answer += (temp + "\n")
    }
};

console.log(answer)