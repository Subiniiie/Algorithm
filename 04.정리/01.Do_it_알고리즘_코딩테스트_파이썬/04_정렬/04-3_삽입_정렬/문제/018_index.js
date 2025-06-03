// 백준 11399

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '018_input.txt')
).toString().trim().split('\n').map((el) => el.trim().split(" ").map(Number));


const N = input[0][0];
let arr = input[1];

for (let i = 1; i < N; i++) {
    let key = arr[i];
    let j = i - 1;

    while (j >= 0 && arr[j] > key) {
        arr[j+1] = arr[j];
        j -= 1;
    };

    arr[j+1] = key;
};

let D = new Array(N).fill(0);
D[0] = arr[0];

for (let i = 1; i < N; i++) {
    D[i] = D[i-1] + arr[i];
};

const result = D.reduce(function add(sum,
    currValue) {
        return sum + currValue;
    }, 0
);

console.log(result)