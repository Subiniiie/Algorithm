const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, 'input.txt')
).toString().trim().split('\n').map((el) => el.trim().split(" ").map(Number));

let arr = Array.from(Array(100), () => new Array(100).fill(0));
const t = Number(input[0][0]);

for (let i = 1; i <= t; i++) {
    const x = input[i][0];
    const y = input[i][1];
    for (let k = 0; k < 10; k++) {
         for (let m = 0; m < 10; m++) {
            const f_x = x + k;
            const f_y = y + m;
            if (arr[f_x][f_y] === 0) {
                arr[f_x][f_y] = 1
            };
         }
    };
};
let a = 0;

for (let i = 0; i < 100; i++) {
        let c = arr[i].filter(e => 1 === e).length;
        a += c;
};


console.log(a)