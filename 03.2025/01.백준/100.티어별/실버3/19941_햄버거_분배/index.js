const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.trim().split(" "));

const N = Number(input[0][0]);
const K = Number(input[0][1]);
const arr = input[1][0];
let answer = 0;
let h = -1;

for (let i = 0; i < N; i++) {
    const p = arr[i];
    if (p === "P") {
        for (let j = i - K; j <= i + K ; j++) {
            if (j >= 0 && j < N && j > h) {
                if (arr[j] === "H") {
                    answer += 1;
                    h = j;
                    break
                };
            };
        };
    };
};

console.log(answer)