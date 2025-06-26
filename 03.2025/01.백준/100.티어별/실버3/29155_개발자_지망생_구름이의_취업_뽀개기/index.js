// 틀림

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, "input.txt")
).toString().trim().split("\n").map((el) => el.trim().split(" "));

const N = Number(input[0][0]);
const P = input[1].map(Number);
let arr = input.slice(2, N+2).map((el) => el.map(Number));

let sortedArr = {};

for (let i = 0; i < arr.length; i++) {
    const a = arr[i][0];
    const b = arr[i][1];

    if (a in sortedArr) {
        sortedArr[a].push(b);
    } else {
        sortedArr[a] = [b];
    };
};

let temp = [];


for (var key in sortedArr) {
    let values = sortedArr[key];
    values.sort((a, b) => a - b)
    
    for (let i = 0; i < P[key - 1]; i++) {
        temp.push(values[i])
    };

    if (P[key - 1] > 0) {
        temp.push(60);
    };
};


let answer = 0;

for (let i = 0; i < temp.length - 1; i++) {
    if (temp[i] !== 60 && temp[i+1] !== 60) {
        answer += (temp[i] + (temp[i+1] - temp[i]));
    } else {
        answer += temp[i];
    };
};

if (temp[temp.length -1] !== 60)  answer += temp[temp.length - 1];

console.log(answer)