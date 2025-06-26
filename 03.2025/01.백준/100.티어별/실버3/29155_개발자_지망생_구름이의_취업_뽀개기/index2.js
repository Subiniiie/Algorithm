const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, "input.txt")
).toString().trim().split("\n").map((el) => el.trim().split(" "));

const N = Number(input[0][0]);
const P = input[1].map(Number);
let arr = input.slice(2, N+2).map((el) => el.map(Number));

let sum = new Array(P.length + 1).fill(0);
sum[1] = P[0];

for (let i = 2; i < P.length + 1; i++) {
    sum[i] = sum[i-1] + P[i-1];
};

console.log(sum)
let times = new Array(sum[sum.length - 1]).fill(0);
console.log(times)

// for (let i = 0; i < arr.length; i++) {
//     const idx = arr[i][0];
//     const value = arr[i][1];

//     if (times.length < sum[idx]) {
//         times.splice()
//     }

//     }
// }

