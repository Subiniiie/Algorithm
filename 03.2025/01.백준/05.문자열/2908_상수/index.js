const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split(" ");


const A = input[0];
const B = input[1];

const reaverseA = Number(A[2] + A[1] + A[0]);
const reaverseB = Number(B[2] + B[1] + B[0]);

if (reaverseA > reaverseB) {
    console.log(reaverseA)
} else {
    console.log(reaverseB)
};