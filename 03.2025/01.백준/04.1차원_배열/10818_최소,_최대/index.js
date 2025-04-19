const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split("\n").map((el) => el.split(" ").map(Number));


console.log(Math.min.apply(null, input[1]) + " " + Math.max.apply(null, input[1]))