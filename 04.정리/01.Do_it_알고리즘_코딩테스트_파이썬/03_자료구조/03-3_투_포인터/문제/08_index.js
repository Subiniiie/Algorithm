// 백준 1253 좋다('좋은 수' 구하기)
// 같은 수가 있다면 어떻게 할 것인가??

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform == 'linux' ?
    '/dev/stdin' : path.join(__dirname, '08_input.txt')
).toString().trim().split("\n").map((el) => el.split(" ").map(Number));

let count = 0;
let sum = 0;
let index = [];
const arr = input[1].sort((a, b) => a - b);

for (let i = 2; i < input[0][0]; i++) {
    let end = i - 1;
    let start = 0;
    while (start < end) {
        sum = arr[start] + arr[end];
        if (sum === arr[i] && start !== end) {
            count += 1;
            start += 1;
            end -= 1;
            break
        } else if (sum < arr[i]) {
            start += 1;
        } else {
            end -= 1;
        };
    };
};

console.log(count)
