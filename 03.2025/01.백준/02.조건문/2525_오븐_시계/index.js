const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.split(" ").map(Number));

let A = input[0][0];
let B = input[0][1];
let C = input[1][0];

let D = B + C;


if (D >= 60) {
    let E = Math.floor(D / 60);
    if (A + E >= 24) {
        A -= (24 - E)
    } else {
        A += E
    }
    D -= (E * 60)
};


console.log(A+" "+D);