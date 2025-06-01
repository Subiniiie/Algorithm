const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(Number))

const N = input[0][0];
const M = input[1][0];
const arr = input[2];


let maxIndex = N - 1;
let minIndex = 0;

let count = 0;
let sum = 0;

arr.sort(function (a, b) {
    return a - b;
});

while (minIndex < maxIndex) {
    sum = arr[minIndex] + arr[maxIndex];
    if (sum === M) {
        minIndex += 1;
        maxIndex -= 1;
        count += 1;
    } else if (sum > M) {
        sum -= arr[maxIndex];
        maxIndex -= 1;
    } else {
        sum -= arr[minIndex];
        minIndex += 1;
    }
};

console.log(count)