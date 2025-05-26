const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();


const n = Number(input);
let c = 1;
let start_index = 1;
let end_index = 1;
let sum = 1;

while (end_index !== n) {
    // 정답 케이스
    if (sum === n) {
        c += 1;
        end_index += 1;
        sum += end_index;
    } else if (sum > n) {
        sum -= start_index;
        start_index += 1;
    } else {
        end_index += 1;
        sum += end_index;
    }
};

console.log(c)