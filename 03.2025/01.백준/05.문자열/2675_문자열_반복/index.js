const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((line) => 
    line.trim().split(' ').map((el) => el.trim()));


const T = Number(input[0][0]);

let a = ''

for (let i = 1; i < T + 1; i++) {
    const c = Number(input[i][0]);
    const s = input[i][1];
    let temp = '';
    for (const element of s) {
        temp += element.repeat(c);
    };
    a += temp;
    if (i < T) {
        a += '\n'
    };
};

console.log(a)