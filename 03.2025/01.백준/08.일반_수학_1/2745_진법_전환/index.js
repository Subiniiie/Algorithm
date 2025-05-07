const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split(" ")

const N = input[0];
const B = Number(input[1]);
const l = N.length;

function binaryNumber(N, l) {
    let a = 0;
    for (let i = l - 1; i >= 0; i--) {
        const t = l - 1 - i;
        if (N[i] === '1') {
            a += 2 ** t;
        };
    };
    return a;
};

function octalNumber(N, l) {
    let a = 0;
    for (let i = l - 1; i >= 0; i--) {
        const t = l - 1 - i;
        a += Number(N[i]) * (8 ** t);
    };
    return a;
};



if (B === 2) {
    console.log(binaryNumber(N, l));
} else if (B === 8) {
    console.log(octalNumber(N, l));
}
