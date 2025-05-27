// 백준 12891 DNA 비밀번호

const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, '009_input.txt')
).toString().trim().split('\n').map((el) => el.trim().split(" "));

const S = Number(input[0][0]);
const P = Number(input[0][1]);
const A = input[1][0];
const checkList = input[2].map(Number);

let myList = new Array(0, 0, 0, 0);
let checkSecret = 0;

let count = 0;


function myadd(c) {
if (c === 'A') {
    myList[0] += 1;
    if (myList[0] === checkList[0]) {
        checkSecret += 1
    }; 
} else if (c === 'C') {
        myList[1] += 1;
        if (myList[1] === checkList[1]) {
            checkSecret += 1
        };
    } else if (c === 'G') {
        myList[2] += 1;
        if (myList[2] === checkList[2]) {
            checkSecret += 1
        };
    } else {
        myList[3] += 1;
        if (myList[3] === checkList[3]) {
            checkSecret += 1
        };
    };
}

function myremove(c) {
if (c === 'A') {
    if (myList[0] === checkList[0]) {
        checkSecret -= 1
    }; 
    myList[0] -= 1;
} else if (c === 'C') {
        if (myList[1] === checkList[1]) {
            checkSecret -= 1
        };
        myList[1] -= 1;
    } else if (c === 'G') {
        if (myList[2] === checkList[2]) {
            checkSecret -= 1
        };
        myList[2] -= 1;
    } else {
        if (myList[3] === checkList[3]) {
            checkSecret -= 1
        };
        myList[3] -= 1;
    };
}


for (let i = 0; i < 4; i++) {
    // 0인 경우 먼저 확인
    if (checkList[i] === 0) {
        checkSecret += 1;
    };
};

// 초기 P 부분
for (let i = 0; i < P; i++) {
    myadd(A[i])
};

if (checkSecret === 4) {
    count += 1;
};

for (let i = P; i < S; i++) {
    // 왼쪽 수 빼기
    let j = i - P;
    myremove(A[j]);
    // 오른쪽 수 더하기
    myadd(A[i]);

    if (checkSecret === 4) {
        count += 1
    };
};

console.log(count)