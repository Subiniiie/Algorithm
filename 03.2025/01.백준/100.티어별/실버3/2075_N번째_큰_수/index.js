const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, "input.txt")
).toString().split("\n").map((el) => el.split(" ").map(Number));

const N = input[0][0];
let sortedArr = [];

function findIdx(n) {
    let mnIdx = 0;
    let mxIdx = sortedArr.length - 1;

    while (mnIdx < mxIdx) {
        const middleIdx = Math.floor((mnIdx + mxIdx) / 2);

        if (n > sortedArr[middleIdx]) mnIdx = middleIdx + 1
        else mxIdx = middleIdx;

    };

    if (mnIdx < sortedArr.length && n > sortedArr[mnIdx]) mnIdx++;

    sortedArr.splice(mnIdx, 0, n);

    if (sortedArr.length > N) {
        sortedArr.shift();
    };

    return sortedArr;
};

for (let i = 1 ; i < N + 1; i++) {
    for (let j = 0; j < N; j++) {
        if (sortedArr.length === 0) {
            sortedArr.push(input[i][j])
        }
        else findIdx(input[i][j]);
    }
}


console.log(sortedArr[0])