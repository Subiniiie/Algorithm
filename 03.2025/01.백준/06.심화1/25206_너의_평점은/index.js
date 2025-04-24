const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.trim().split(" "));


let s = 0;
let t = 0;
const grade = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
    'F': 0.0,
};

for (let i = 0; i < 20; i++) {
    if (input[i][2] === 'P') {
        continue;
    } else {
        const temp = Number(input[i][1]) * grade[input[i][2]];
        s += temp;
        t += Number(input[i][1]);
    };
};

console.log(s / t)
