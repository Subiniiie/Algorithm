// 백준 1940 주몽

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '07_input.txt')
).toString().trim().split('\n').map((el) => el.split(" ").map(Number));

let m = input[1][0];
let sum = 0;
let count = 0;
let start_index = 0;
let end_index = input[0][0] - 1;

const arr = input[2].sort((a, b) => {
    return a - b
});

while (end_index > start_index) {
    sum = arr[start_index] + arr[end_index];
    if (sum === m) {
        count += 1;
        start_index += 1;
        end_index -= 1;
    } else if (sum < m) {
        start_index += 1;
    } else {
        end_index -= 1;
    };
};

console.log(count)