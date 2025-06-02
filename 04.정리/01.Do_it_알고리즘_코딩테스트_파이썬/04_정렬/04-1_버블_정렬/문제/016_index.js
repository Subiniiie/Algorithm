// 백준 1377 버블 정렬 프로그램1

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '016_input.txt')
).toString().trim().split("\n").map((el) => el.trim()).map(Number);

const N = input[0];
let prevIndex = new Array();

for (let i = 0; i < N; i++) {
    prevIndex.push([i, input[i+1]]);
};

const nextIndex = [...prevIndex].sort(function (a, b) {
    return a[1] - b[1]
});

let maxChange = 0;

for (let i = 0; i < N; i++) {
    const temp = nextIndex[i][0] - i;
    if (maxChange < temp) {
        maxChange = temp
    };
};

console.log(maxChange+1)