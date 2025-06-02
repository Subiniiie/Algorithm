// 백준 2750 수 정렬하기1

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '015_input.txt')
).toString().trim().split("\n").map((el) => el.trim()).map(Number);

let N = input[0];
let arr = new Array();

for (let i = 1; i <= N; i++) {
    arr.push(input[i])
};


for (let i = 0; i < N; i++) {
    for (let j = 0; j < N-1-i; j++) {
        if (arr[j] > arr[j+1]) {
            [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
        };
    };
};

let answer = "";
for (let element of arr) {
    answer += (element + "\n")
}

console.log(answer)