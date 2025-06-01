const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(Number));

const N = input[0][0];
const M = input[0][1];

let arr = new Array();
let sections = new Array();

for (let i = 1; i < input.length; i++) {
    if (i <= N) {
        arr.push(input[i])
    } else {
        sections.push(input[i])
    }
};

let D = Array.from(Array(N+1), () => Array(N+1).fill(0))
D[1][1] = arr[0][0];

for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        if (i === 0 && j > 0) {
            D[i+1][j+1] = D[i+1][j] + arr[i][j];
        } else if (i > 0 && j === 0) {
            D[i+1][j+1] = D[i][j+1] + arr[i][j];
        } else if (i > 0 && j > 0) {
            D[i+1][j+1] = D[i][j+1] + D[i+1][j] + arr[i][j] - D[i][j]
        }
    }
};

let answer = "";

for (let i = 0; i < M; i++) {
    const [x1, y1, x2, y2] = sections[i]
    const temp = D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1]
    answer += (temp + "\n")
};

console.log(answer)