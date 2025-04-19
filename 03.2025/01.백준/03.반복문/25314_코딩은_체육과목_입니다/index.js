const fs = require('fs');
const path = require('path');

const input = +fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim();

let n = Math.floor(input / 4);

for (let i = 0; i < n; i++) {
    process.stdout.write("long ");
};

process.stdout.write('int');