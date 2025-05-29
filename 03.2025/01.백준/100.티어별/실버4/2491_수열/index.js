const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(Number));

const N = input[0][0];
const arr = input[1];

function bigger(arr) {
    let start = 0;
    let maxNum = 0;
    let maxCount = 0;

    for (let i = 0; i < N; i++) {
        if (start <= arr[i]) {
            start = arr[i];
            maxCount += 1;
            maxNum = Math.max(maxNum, maxCount)
        } else {
            maxCount = 1;
            start = arr[i];
        }
    }

    
    return maxNum;
}

function smaller(arr) {
    let start = 100001;
    let minNum = 0;
    let minCount = 0;
    
    for (let i = 0; i < N; i++) {
        if (arr[i] <= start) {
            start = arr[i];
            minCount += 1;
            minNum = Math.max(minNum, minCount);
        } else {
            minCount = 1;
            start = arr[i];
        }
    }

    return minNum;
};

console.log(Math.max(bigger(arr), smaller(arr)))