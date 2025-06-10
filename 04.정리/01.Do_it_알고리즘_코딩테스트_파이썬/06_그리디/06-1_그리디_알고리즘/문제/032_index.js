// 백준 11047

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '032_input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(Number));


const N = input[0][0];
let K = input[0][1];
let arr = new Array();

for (let i = 1; i <= N; i++) {
    arr.push(input[i][0]);
};

let answer = 0;

for (let i = N; i >= 0; i--) {
    if (K >= arr[i]) {
        answer += Math.floor(K / arr[i]);
        K = K % arr[i];
    };
};

console.log(answer)