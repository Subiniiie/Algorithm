// 백준 1427

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '017_input.txt')
).toString().trim().split("").map(Number);

const N = input.length;

for (let i = 0; i < N-1; i++) {
    let maxNum = i+1;
    for (let j = i+1; j < N; j++) {
        if (input[maxNum] < input[j]) {
            maxNum = j;
        };
    };
    if (input[maxNum] > input[i]) {
        [input[maxNum], input[i]] = [input[i], input[maxNum]];
    };
};

let answer = "";

for (element of input) {
    answer += element;
};

console.log(answer)