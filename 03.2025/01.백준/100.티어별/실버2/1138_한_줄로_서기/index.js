const fs = require('fs');
const path = require('path');
const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(Number));

const N = input[0][0];
const arr = input[1];
let temp = new Array();

for (let i = N - 1; i >= 0; i--) {
    const v = arr[i];
    temp.splice(v, 0, i + 1);
};

console.log(temp.join(" "))