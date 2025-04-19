const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.split(' ').map(Number));

let a = '';


for (const element of input) {
    if (element.length > 1) {
        a += element[0] + element[1] + '\n'
    };
};

console.log(a)