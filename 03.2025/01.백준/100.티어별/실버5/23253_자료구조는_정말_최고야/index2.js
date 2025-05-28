const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.trim().split(' ').map(Number))

const N = input[0][0];
const M = input[0][1];

let check = true;

for (let i = 2; i < input.length; i += 2) {
    const temp = input[i];
    const k = temp.length
    for (let j = 0; j < k - 1; j++) {
        if (temp[j] < temp[j + 1]) {
            check = false;
            break;
        }
    }
    if (!check) {
        break;
    }
}

console.log(check ? 'Yes' : 'No')