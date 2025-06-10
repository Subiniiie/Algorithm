const fs = require('fs');
const path = require('path');
const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(BigInt));

const N = input[0][0];
const road = input[1];
const city = input[2];

let answer = 0n;
let curPrice = city[0];

for (let i = 0; i < Number(N) - 1; i++) {
    answer += curPrice * road[i];
    if (curPrice > city[i+1]) curPrice = city[i+1];
};

console.log(answer.toString())