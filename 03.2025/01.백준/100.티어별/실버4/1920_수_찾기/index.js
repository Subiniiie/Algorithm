const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(Number));

const N = input[0][0];
const A = input[1];
const M = input[3];

A.sort(function(a, b) {
    if (a > b) return 1;
    if (a === b) return 0;
    if (a < b) return -1;
});

function GoSorted (num) {
    let start = 0;
    let end = N - 1;
    let c = false;

    while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        let midV = A[mid];

        if (num < midV) {
            end = mid - 1;
        } else if (num > midV) {
            start = mid + 1;
        } else {
            c = true;
            break;
        };
    };

    if (c) {
        return 1;
    } else {
        return 0;
    };
};

let answer = "";

for (let v of M) {
    answer += (GoSorted(v) + "\n");
};

console.log(answer)