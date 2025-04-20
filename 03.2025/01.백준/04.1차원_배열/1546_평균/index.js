const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.split(" ").map(Number));

const temp = input[1];
let maxNum = Math.max.apply(null, temp);

let arr = [];
for (let i = 0; i < temp.length; i++) {
    arr.push(temp[i] / maxNum * 100);
};

function solution(arr) {
    let answer = 0;
    let sum = 0;

    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    };
    return answer = sum / arr.length;
};

console.log(solution(arr))
