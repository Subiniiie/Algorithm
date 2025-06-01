const fs = require('fs');
const path = require('path');
const { start } = require('repl');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

const N = Number(input);

let count = 1;

let startIndex = 1;
let endIndex = 2;
let sum = startIndex + endIndex;

while (endIndex < N) {
    if (sum === N) {
        endIndex += 1;
        sum += endIndex;
        count += 1;
    } else if (sum < N) {
        endIndex += 1;
        sum += endIndex;
    } else {
        sum -= startIndex;
        startIndex += 1;
    }
};

console.log(count)