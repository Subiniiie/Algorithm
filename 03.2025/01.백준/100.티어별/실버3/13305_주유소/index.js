// 왜 오른쪽에서부터 찾으면 안되는지 모르겠음

const fs = require('fs');
const path = require('path');
const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" ").map(BigInt));

const N = input[0][0];
const road = input[1];
const city = input[2];

let end = Number(N) - 2;

let answer = 0n;



while (end >= 0) {
    let minV = 10001n;
    let minI = 0;

    for (let i = end; i >= 0; i--) {
        if (minV > city[i]) {
            minV = city[i];
            minI = i;
        };
    };

    let tempSum = 0n;

    for (let i = end; i >= minI; i--) {
        tempSum += road[i];
    };

    answer += (tempSum * minV);


    end = minI - 1;
};

console.log(answer.toString())